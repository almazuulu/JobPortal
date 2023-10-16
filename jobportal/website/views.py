import os
import certifi
from django.shortcuts import render, redirect
from jobs.models import Country, JobPosition
from jobs.views import countries, companies, job_areas, browse_job_by_filter
from utilities.paginator_page import paginate_queryset
from blog.views import topRecentNews
from django.db.models import Count
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    countries_with_job_counts = Country.objects.annotate(num_jobs=Count('job_positions'))
    
    recent_jobsList = JobPosition.objects.order_by('-posted_date')[:5]
    recent_jobs = paginate_queryset(request, recent_jobsList, 3)
    
    context = {
        'countries': countries_with_job_counts,
        'companies': companies,
        'job_areas': job_areas,
        'recent_jobs': recent_jobs,
    }
    return render(request, 'website/index.html', context)


def about(request):
    context = {
        'topRecentNews': topRecentNews,
    }
    return render(request, 'website/about.html', context)


def contact(request):
    # Устанавливаем пусть к сертификату
    os.environ['SSL_CERT_FILE'] = certifi.where()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Message from {}'.format(form.cleaned_data['dzName'])
            message = 'Sender email: {}\n\nMessage:\n{}'.format(form.cleaned_data['dzEmail'], form.cleaned_data['dzSubject'])
            from_email = form.cleaned_data['dzEmail']
            to_email = [settings.EMAIL_HOST_USER]
            
            send_mail(subject, message, from_email, to_email)
            
            message.success(request, 'Your message has been sent successfully!')
            return redirect('website:contact')
    else:
        form = ContactForm()
            
    context = {
        'form': form,
    }
    return render(request, 'website/contact.html', context)


