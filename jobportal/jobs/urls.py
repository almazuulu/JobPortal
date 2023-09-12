from django.urls import path
from .views import alljobs, browse_job_by_country, job_details

urlpatterns = [
    path("", alljobs, name='jobs'),
    path("country/<str:country_name>", browse_job_by_country, name='jobs_by_country'),
    path("<int:job_id>/", job_details, name='job_details'),
    
]