from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import UserProfile, CandidateProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        

class UserProfileForm(forms.ModelForm):    
    class Meta:
        model = UserProfile
        fields = ['phone', 'profile_image', 'date_of_birth', 'address', 'city', 'country', 'postal_code']
        
        
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        exclude = ('user_profile',)
        




