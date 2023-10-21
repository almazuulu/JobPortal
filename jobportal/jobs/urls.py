from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllJobsView.as_view(), name='jobs'),
    path("country/<str:country_name>", views.browse_job_by_country, name='jobs_by_country'),
    path("company/<str:company_name>", views.browse_job_by_company, name='jobs_by_company'),
    path('category/<str:category_name>/', views.browse_job_by_category, name='job_by_category'),
    path("job_search_results/", views.JobSearchView.as_view(), name='job_search_results'),
    path("<int:job_id>/", views.JobDetailsView.as_view(), name='job_details'),
]