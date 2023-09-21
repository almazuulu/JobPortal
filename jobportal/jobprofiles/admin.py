from django.contrib import admin
from .models import CandidateProfile, UserProfile
from django.utils.html import format_html

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'fullname', 'city', 'country']
    list_display_links = ['fullname']
    
    def fullname(self, obj):
        return obj.user.first_name + " " + obj.user.last_name
    fullname.short_description = "Full Name"
    
    def thumbnail(self, object):
        if object.profile_image and hasattr(object.profile_image, 'file'):
            html_code = '<img src = "{}" width = "25px;" style = "border-radius: 50px;"/>'
            return format_html(html_code.format(object.profile_image.url))
        return "No Image"
    
    
@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'expected_salary']
    list_display_links = ['full_name']
    
    # def fullname(self, obj):
    #     return obj.user_profile.user.first_name + " " + obj.user_profile.user.last_name
    # fullname.short_description = "Full Name"

    
    def email(self, obj):
        return obj.user_profile.user.email 
    
    
