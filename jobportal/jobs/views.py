from django.shortcuts import render, get_object_or_404
from .models import Country, Company, JobPosition
from blog.views import topRecentNews

countries = Country.objects.all

def alljobs(request):
    context = {
        'titlepage': 'All jobs',
        'countries': countries,
    }
    return render(request, 'jobs/jobs.html', context)


def browse_job_by_country(request, country_name=None):
    if country_name:
        country = Country.objects.get(country_name=country_name)
        jobs = JobPosition.objects.filter(country=country, is_active=True)
    else:
        jobs = JobPosition.objects.filter(is_active=True)
        
    context = {
        'jobs': jobs,
        'countries': countries,
        'selected_country': country_name,
    }
    
    return render(request, 'jobs/jobs_list.html', context)


def job_details(request, job_id):
    job = get_object_or_404(JobPosition, id=job_id)
    
    context = {
        'job': job,
        'topRecentNews': topRecentNews,
    }
    
    return render(request, 'jobs/job_detail.html', context)
        
    
        
