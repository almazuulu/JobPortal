from django.shortcuts import render, redirect, get_object_or_404
from .models import CandidateProfile, CompanyProfile
from utilities.paginator_page import paginate_queryset
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm, CandidateProfileForm, ChangePasswordForm, CompanyProfileForm, JobPositionForm
from jobs.models import JobPosition
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseForbidden


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        username = username.lower()
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    
    return render(request, 'jobprofiles/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        user_form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if form_type == 'candidate':
            candidate_form = CandidateProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid() and candidate_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                candidate = candidate_form.save(commit=False)
                candidate.user_profile = profile
                candidate.save()
                applied_jobs_ids = request.POST.getlist('applied_jobs')
                saved_jobs_ids = request.POST.getlist('favorited_jobs')
                
                # Получаем объекты JobPosition и сохраняем 
                applied_jobs = JobPosition.objects.filter(id__in=applied_jobs_ids)
                saved_jobs = JobPosition.objects.filter(id__in=saved_jobs_ids)
                
                candidate.applied_jobs.set(applied_jobs)
                candidate.favorited_jobs.set(saved_jobs)
                return redirect('login')
                
        elif form_type == 'company':
            company_form = CompanyProfileForm(request.POST)
            if user_form.is_valid() and profile_form.is_valid() and company_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                company = company_form.save(commit=False)
                company.user_profile = profile
                company.save()
                # Обработка других полей и редирект, если необходимо
                return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = UserProfileForm()
        candidate_form = CandidateProfileForm()
        company_form = CompanyProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'candidate_form': candidate_form,
        'company_form': company_form
    }

    return render(request, 'jobprofiles/register.html', context)


@login_required(login_url='login')
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            user = form.save()
            
            # Обновляем сессию, чтобы пользов не выходил из системы после смены пароля
            update_session_auth_hash(request, form.user)
            return redirect('login')
    else:
        form = ChangePasswordForm(request.user)
        
    return render(request, 'jobprofiles/change_password.html', {'form': form})
            
            
            
@login_required(login_url='login')
def candidate_profile(request, candidate_id):
    candidate = CandidateProfile.objects.get(id = candidate_id)
    context = {
        'candidate': candidate,
    }
    return render(request, 'jobprofiles/candidate_profile.html', context)

@login_required(login_url='login')
def candidate_applied_jobs(request, candidate_id):
    candidate = CandidateProfile.objects.get(id = candidate_id)
    applied_jobList = candidate.applied_jobs.all()
    applied_jobs = paginate_queryset(request, applied_jobList, 3)
    
    context = {
        'candidate': candidate,
        'applied_jobs': applied_jobs,
    }
    
    return render(request, 'jobprofiles/candidate_applied_jobs.html', context)
    
@login_required(login_url='login')
def candidate_saved_jobs(request, candidate_id):
    candidate = CandidateProfile.objects.get(id = candidate_id)
    saved_jobList = candidate.favorited_jobs.all()
    savedJobs = paginate_queryset(request, saved_jobList, 2)
    
    context = {
        'candidate': candidate,
        'savedJobs': savedJobs,
    }
    
    return render(request, 'jobprofiles/candidate_saved_jobs.html', context)

# Company Profile
def company_profile(request, company_id):
    company = CompanyProfile.objects.get(id=company_id)
    context = {
        'company': company
    }
    return render(request, 'jobprofiles/company_profile.html', context)

def manage_jobs(request, company_id):
    company = get_object_or_404(CompanyProfile, id=company_id)
    jobsList = JobPosition.objects.filter(company=company)
    jobs = paginate_queryset(request, jobsList, 3)
    
    context = {
        'company': company,
        'jobs': jobs,
    }
    return render(request, 'jobprofiles/company_manage_job.html', context)


def delete_job(request, job_id):
    job = get_object_or_404(JobPosition, id=job_id)
    company = job.company.id
    job.delete()
    
    return redirect('manage_jobs', company)


def company_resume(request):
    context = {
        
    }
    return render(request, 'jobprofiles/company_resume.html', context)
    
    
def post_job(request):
    user = request.user
    company_id = user.userprofile.companyprofile.id
    
    if not(hasattr(user, 'userprofile') and hasattr(user.userprofile, 'companyprofile')):
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        form = JobPositionForm(request.POST, request.FILES)
        if form.is_valid():
            job_position = form.save(commit=False)
            job_position.company = user.userprofile.companyprofile
            job_position.save()
            
            return redirect('manage_jobs', company_id)
    else:
        form = JobPositionForm()
        
    context = {
        'form': form,
    }
    return render(request, 'jobprofiles/company_post_jobs.html', context)
    
    