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

def job_details(request, job_id):
    job = get_object_or_404(JobPosition, id=job_id)
    
    context = {
        'job': job,
        'topRecentNews': topRecentNews,
    }
    
    return render(request, 'jobs/job_detail.html', context)


# Представления для обработки различных фильтров
def browse_job_by_country(request, country_name=None):
    return browse_job_by_filter(request, 'country', country_name)

def browse_job_by_company(request, company_name=None):
    return browse_job_by_filter(request, 'company', company_name)


# Функция обобщенных представлений по фильтрам
def browse_job_by_filter(request, filter_type=None, filter_value=None):
    if filter_type == 'country':
        queryset = JobPosition.objects.filter(country__country_name=filter_value, is_active=True)
    elif filter_type == 'company':
        queryset = JobPosition.objects.filter(company__company_name=filter_value)
    else:
        queryset = JobPosition.objects.filter(is_active=True)
    return get_jobs_list(request, queryset)


# Функция для получения списка вакансий и перенаправление в шаблоны
def get_jobs_list(request, queryset, items_per_page=2):
    jobs = paginate_queryset(request, queryset, items_per_page)
    context = {
        'jobs': jobs,
        'countries': countries,
        'companies': companies,
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

    return get_jobs_list(request, jobList, 4)

    
        
