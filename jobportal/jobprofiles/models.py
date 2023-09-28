from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    profile_image = models.ImageField(upload_to='photos/users/', blank=True, null=True, default='photos/comments/userdef.png')
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def is_candidate(self):
        return hasattr(self, 'candidateprofile')
    
    def is_company(self):
        return hasattr(self, 'companyprofile')
    
    
class CandidateProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    age = models.IntegerField(null=True, blank=True)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    languages = models.CharField(max_length=255, blank=True, null=True)
    current_job_title = models.CharField(max_length=255, blank=True)
    current_salary = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    expected_salary = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    applied_jobs = models.ManyToManyField('jobs.JobPosition', related_name='applicants', blank=True)
    favorited_jobs = models.ManyToManyField('jobs.JobPosition', related_name='favorited_by', blank=True)
    
    
    def full_name(self):
        return self.user_profile.user.get_full_name()
    
    def email(self):
        return self.user_profile.user.email
    
    
class CompanyProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
      
    # Social Links
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name
    
    def founded_date(self):
        return self.user_profile.date_of_birth

    def country (self):
        return self.user_profile.country
        
    def email(self):
        return self.user_profile.user.email
    
    def city(self):
        return self.user_profile.city
    
    def company_logo(self):
        return self.user_profile.profile_image

    def full_name(self):
        return self.user_profile.user.get_full_name()
    