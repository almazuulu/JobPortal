from django.urls import path
from .views import alljobs, browse_job_by_country, job_details, browse_job_by_company

urlpatterns = [
    path("", alljobs, name='jobs'),
    path("country/<str:country_name>", browse_job_by_country, name='jobs_by_country'),
    path("company/<str:company_name>", browse_job_by_company, name='jobs_by_company'),
    path("<int:job_id>/", job_details, name='job_details'),
    
]