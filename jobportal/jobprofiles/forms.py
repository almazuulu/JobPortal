from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, CandidateProfile, CompanyProfile
from django.contrib.auth.forms import PasswordChangeForm
from jobs.models import JobPosition

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):           
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Type Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

        
class UserProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ['phone', 'profile_image', 'date_of_birth', 'address', 'city', 'country', 'postal_code']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'type': 'date'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
        }
        
        
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        exclude = ('user_profile',)
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'languages': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Languages'}),
            'current_job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Job Title'}),
            'current_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current Salary'}),
            'expected_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Expected Salary'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        
class CompanyProfileForm(forms.ModelForm):
    
    class Meta:
        model = CompanyProfile
        exclude = ('user_profile',)
        fields = [
            'company_name', 
            'website', 
            'description', 
            'facebook', 
            'twitter', 
            'google', 
            'linkedin'
        ]
        
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Facebook URL'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Twitter URL'}),
            'google': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Google URL'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'LinkedIn URL'}),
        }
        

class JobPositionForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        exclude = ('company',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Area'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Industry'}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minimum Salary'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Maximum Salary'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}),
            'job_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description'}),
            'how_to_apply': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How to Apply'}),
            'job_requirements': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Requirements'}),
            'skill': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skills'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
        }