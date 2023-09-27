from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path('register/', views.register, name = 'register'),
    path('change_password/', views.change_password, name = 'change_password'),
    
    # Candidate
    path('candidate/<uuid:candidate_id>/', views.candidate_profile, name='candidate_profile'),
    path('candidate/applied_jobs/<uuid:candidate_id>/', views.candidate_applied_jobs, name='candidate_applied_jobs'),
    path('candidate/saved_jobs/<uuid:candidate_id>/', views.candidate_saved_jobs, name='candidate_saved_jobs'),
    
    # Company
    path('company/<int:company_id>', views.company_profile, name='company_profile'),
    path('company/manage_jobs/<int:company_id>', views.manage_jobs, name='manage_jobs'),
    path('company/company_resume/', views.company_resume, name='company_resume'),
    path('company/post_job/', views.post_job, name='post_job'),
]
