from django.urls import path
from .views import AllJobsView, browse_job_by_country, JobDetailsView, browse_job_by_company, job_search_result

urlpatterns = [
    path("", AllJobsView.as_view(), name='jobs'),
    path("country/<str:country_name>", browse_job_by_country, name='jobs_by_country'),
    path("company/<str:company_name>", browse_job_by_company, name='jobs_by_company'),
    path("job_search_results/", job_search_result, name='job_search_results'),
    path("<int:job_id>/", JobDetailsView.as_view(), name='job_details'),
]