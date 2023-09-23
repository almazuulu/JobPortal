from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path('register/', views.register, name = 'register'),
    path('change_password/', views.change_password, name = 'change_password'),
    path('<uuid:candidate_id>/', views.candidate_profile, name='candidate_profile'),
    path('applied_jobs/<uuid:candidate_id>/', views.candidate_applied_jobs, name='candidate_applied_jobs'),
    path('saved_jobs/<uuid:candidate_id>/', views.candidate_saved_jobs, name='candidate_saved_jobs'),
]
