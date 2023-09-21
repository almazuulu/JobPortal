from django.urls import path
from . import views


urlpatterns = [
    path('<uuid:candidate_id>/', views.candidate_profile, name='candidate_profile'),
    path('applied_jobs/<uuid:candidate_id>/', views.candidate_applied_jobs, name='candidate_applied_jobs'),
    path('saved_jobs/<uuid:candidate_id>/', views.candidate_saved_jobs, name='candidate_saved_jobs'),
]
