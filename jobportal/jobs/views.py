from django.shortcuts import render, get_object_or_404
from .models import Country, Company, JobPosition
from blog.views import topRecentNews
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utilities.paginator_page import paginate_queryset

countries = Country.objects.all()
companies = Company.objects.all()
job_areas = JobPosition.objects.values_list('area', flat=True).distinct().exclude(area__isnull=True).exclude(area='')

def alljobs(request):
    context = {
        'titlepage': 'All jobs',
        'countries': countries,
        'companies': companies,
    }
    return render(request, 'jobs/jobs.html', context)

# def alljobs(request):
#     search_keywords = request.GET.get('keywords', '')
#     search_locations = request.GET.get('location', '')
    
#     jobList = JobPosition.objects.filter(
#         title__icontains=search_keywords,
#         location__icontains=search_locations,
#         is_active=True)
    
#     jobs = paginate_queryset(request, jobList, 4)
    
#     context = {
#         'titlepage': 'All jobs',
#         'countries': countries,
#         'companies': companies,
#         'jobs': jobs,
#     }
#     return render(request, 'jobs/jobs.html', context)


def browse_job_by_country(request, country_name=None):
    if country_name:
        country = Country.objects.get(country_name=country_name)
        jobList = JobPosition.objects.filter(country=country, is_active=True)
    else:
        jobList = JobPosition.objects.filter(is_active=True)
    
    jobs = paginate_queryset(request, jobList, 2)
        
    context = {
        'jobs': jobs,
        'countries': countries,
        'companies': companies,
        'selected_country': country_name,
        'job_areas': job_areas,
    }
    
    return render(request, 'jobs/jobs_list.html', context)


def job_details(request, job_id):
    job = get_object_or_404(JobPosition, id=job_id)
    
    context = {
        'job': job,
        'topRecentNews': topRecentNews,
    }
    
    return render(request, 'jobs/job_detail.html', context)

def browse_job_by_company(request, company_name):
    company_name = Company.objects.get(company_name=company_name)
    jobList = JobPosition.objects.filter(company=company_name)
    
    jobs = paginate_queryset(request, jobList, 2)
        
    context = {
        'jobs': jobs,
        'countries': countries,
        'companies': companies,
        'selected_company': company_name,
        'job_areas': job_areas,
    }
    
    return render(request, 'jobs/jobs_list.html', context)


def job_search_result(request):
    search_area = request.GET.get('job_area_name')
    search_keywords = request.GET.get('keywords', '')
    search_locations = request.GET.get('location', '')
    
    filters = {
        'title__icontains': search_keywords,
        'location__icontains': search_locations,
        'is_active': True,
    }
    
    if search_area and search_area != "Select Sector":
        filters['area__icontains'] = search_area
    
    jobList = JobPosition.objects.filter(**filters)
    
    jobs = paginate_queryset(request, jobList, 4)
    
    context = {
        'countries': countries,
        'companies': companies,
        'jobs': jobs,
        'job_areas': job_areas,
    }
    
    return render(request, 'jobs/jobs_list_results.html', context)
    
        
