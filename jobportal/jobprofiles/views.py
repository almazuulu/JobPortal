from typing import Any
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import CandidateProfile, CompanyProfile, UserProfile
from utilities.paginator_page import paginate_queryset
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm, CandidateProfileForm, ChangePasswordForm, CompanyProfileForm, JobPositionForm
from jobs.models import JobPosition
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseForbidden
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import FormView, DeleteView, CreateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy




# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         username = username.lower()
#         password = request.POST['password']
        
#         user = auth.authenticate(username = username, password = password)
        
#         if user:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return redirect('login')
    
#     return render(request, 'jobprofiles/login.html')


class LoginView(TemplateView):
    template_name = 'jobprofiles/login.html'
    success_url = 'home'
    error_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Если вы хотите передать дополнительный контекст в шаблон, добавьте его здесь.
        # Например: context['error_message'] = "Invalid login credentials"
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '').lower()
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
        
        if user:
            auth.login(request, user)
            messages.success(request, f'Dear {username} you are successfully loged in!')
            return redirect(self.success_url)
        else:
            messages.error(request, f'Incorrect username or password')
            return redirect(self.error_url)
        
# def logout(request):
#     auth.logout(request)
#     return redirect('login')

class LogoutView(View):
    redirect_url = 'login'
    
    def get(self, request, *args, **kwargs):
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


# @login_required(login_url='login')
# def change_password(request):
#     user = request.user
#     if request.method == 'POST':
#         form = ChangePasswordForm(user=request.user, data=request.POST)
        
#         if form.is_valid():
#             user = form.save()
            
#             # Обновляем сессию, чтобы пользов не выходил из системы после смены пароля
#             update_session_auth_hash(request, form.user)
#             return redirect('login')
#     else:
#         form = ChangePasswordForm(request.user)
        
#     return render(request, 'jobprofiles/change_password.html', {'form': form})


@method_decorator(login_required(login_url='login'), name='dispatch')
class ChangePasswordView(FormView):
    template_name = 'jobprofiles/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('login')   
    
    def get_form_kwargs(self):
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        
        return kwargs
    
    def form_valid(self, form):
         user = form.save()
         # Обновляем сессию, чтобы пользов не выходил из системы после смены пароля
         update_session_auth_hash(self.request, form.user)
         
         messages.success(self.request, f'Dear {user.username} your password was successfully chaged! Please Login again!')
         return super(ChangePasswordView, self).form_valid(form)
                
            
@login_required(login_url='login')
def candidate_profile(request, candidate_id):
    candidate = CandidateProfile.objects.get(id = candidate_id)
    context = {
        'candidate': candidate,
    }
    return render(request, 'jobprofiles/candidate_profile.html', context)


# @login_required(login_url='login')
# def candidate_applied_jobs(request, candidate_id):
#     candidate = CandidateProfile.objects.get(id = candidate_id)
#     applied_jobList = candidate.applied_jobs.all()
#     applied_jobs = paginate_queryset(request, applied_jobList, 3)
    
#     context = {
#         'candidate': candidate,
#         'applied_jobs': applied_jobs,
#     }
    
#     return render(request, 'jobprofiles/candidate_applied_jobs.html', context)


# @login_required(login_url='login')
# def candidate_saved_jobs(request, candidate_id):
#     candidate = CandidateProfile.objects.get(id = candidate_id)
#     saved_jobList = candidate.favorited_jobs.all()
#     savedJobs = paginate_queryset(request, saved_jobList, 2)
    
#     context = {
#         'candidate': candidate,
#         'savedJobs': savedJobs,
#     }
    
#     return render(request, 'jobprofiles/candidate_saved_jobs.html', context)

@method_decorator(login_required(login_url='login'), name='dispatch')
class CandidateJobsBasedView(TemplateView):
    
    def get_jobs(self, candidate):
        raise NotImplementedError
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        candidate_id = kwargs.get('candidate_id')
        candidate = CandidateProfile.objects.get(id = candidate_id)
        jobList = self.get_jobs(candidate)
        jobs = paginate_queryset(self.request, jobList, 2)
        
        context['candidate'] = candidate
        context['jobs'] = jobs
        
        return context
        
    
class CandidateAppliedJobsView(CandidateJobsBasedView):
    template_name = 'jobprofiles/candidate_applied_jobs.html'
    
    def get_jobs(self, candidate):
        return candidate.applied_jobs.all()
    
    
class CandidateSavedJobsView(CandidateJobsBasedView):
    template_name = 'jobprofiles/candidate_saved_jobs.html'
    
    def get_jobs(self, candidate):
        return candidate.favorited_jobs.all()
    

@login_required(login_url='login')
def apply_for_job(request, job_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if not user_profile.is_candidate():
        return HttpResponseForbidden('User is not candidate!')
    
    candidate_profile = user_profile.candidateprofile
    job = get_object_or_404(JobPosition, id=job_id)
    candidate_profile.applied_jobs.add(job)
    messages.success(request, f'Dear {user_profile.user.first_name} you successfully applied for {job.title} at {job.company.company_name}!')
    return redirect('candidate_applied_jobs', candidate_profile.id)


@login_required(login_url='login')
def save_job(request, job_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if not user_profile.is_candidate():
        return HttpResponseForbidden('User is not candidate!')
    
    candidate_profile = user_profile.candidateprofile
    job = get_object_or_404(JobPosition, id=job_id)
    candidate_profile.favorited_jobs.add(job)
    messages.success(request, f'{job.title} was successfully saved in your profile!')
    return redirect('candidate_saved_jobs', candidate_profile.id)


@login_required(login_url='login')
def remove_favorited_job(request, job_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if not user_profile.is_candidate():
        return HttpResponseForbidden('User is not candidate!')
    
    job = get_object_or_404(JobPosition, id=job_id)
    candidate_profile = user_profile.candidateprofile
    candidate_profile.favorited_jobs.remove(job)
    messages.success(request, f'{job.title} from {job.company.company_name} was successfully removed from saved!')
    return redirect('candidate_saved_jobs', candidate_profile.id)



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


# def delete_job(request, job_id):
#     job = get_object_or_404(JobPosition, id=job_id)
#     company = job.company.id
#     job.delete()
    
#     return redirect('manage_jobs', company)

@method_decorator(login_required(login_url='login'), name='dispatch')
class JobDeleteView(DeleteView):
    model = JobPosition
    
    def get_object(self, query_set=None):
        return get_object_or_404(JobPosition, id= self.kwargs['job_id'])
    
    def get_success_url(self) -> str:
        company = self.object.company.id
        return reverse_lazy('manage_jobs', args=[company])
        
        
@login_required(login_url='login')
def edit_job(request, job_id):
    user = request.user
    company_id = user.userprofile.companyprofile.id
    
    job = get_object_or_404(JobPosition, id=job_id)
    if request.method == 'POST':
        form = JobPositionForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, f'{job.title} was successfully updated!')
            return redirect('manage_jobs', company_id)
        else:
            form = JobPositionForm(instance=job)
    
    context = {
        'form': form,
        'job': job,
    }
    
    return render(request, 'jobprofiles/company_edit_job.html', context)
        


def company_resume(request):
    user = request.user
    if not(hasattr(user, 'userprofile') and hasattr(user.userprofile, 'companyprofile')):
        return HttpResponseForbidden()
    
    company_profile = CompanyProfile.objects.get(user_profile__user=user)
    job_positions = JobPosition.objects.filter(company=company_profile)
    applicantsList = CandidateProfile.objects.filter(applied_jobs__in=job_positions).distinct()
    applicants =  paginate_queryset(request, applicantsList, 3)
    
    context = {
        'applicants': applicants,
    }
    return render(request, 'jobprofiles/company_resume.html', context)
    


# def post_job(request):
#     user = request.user
#     company_id = user.userprofile.companyprofile.id
    
#     if not(hasattr(user, 'userprofile') and hasattr(user.userprofile, 'companyprofile')):
#         return HttpResponseForbidden()
    
#     if request.method == 'POST':
#         form = JobPositionForm(request.POST, request.FILES)
#         if form.is_valid():
#             job_position = form.save(commit=False)
#             job_position.company = user.userprofile.companyprofile
#             job_position.save()
            
#             return redirect('manage_jobs', company_id)
#     else:
#         form = JobPositionForm()
        
#     context = {
#         'form': form,
#     }
#     return render(request, 'jobprofiles/company_post_jobs.html', context)    
@method_decorator(login_required(login_url='login'), name='dispatch')
class PostJobView(CreateView):   
    model = JobPosition
    form_class = JobPositionForm
    template_name = 'jobprofiles/company_post_jobs.html'
    success_url = 'manage_jobs'
     
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not (hasattr(user, 'userprofile') and hasattr(user.userprofile, 'companyprofile')):
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        job_position = form.save(commit=False)
        job_position.company = self.request.user.userprofile.companyprofile
        messages.success(self.request, f'{job_position} inn {job_position.company.company_name} was published successfully!' )
        self.success_url = reverse_lazy('manage_jobs', args=[self.request.user.userprofile.companyprofile.id])
        return super().form_valid(form)
    
    
     

    