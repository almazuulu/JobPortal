from django.contrib import admin
from .models import Country, JobPosition
from django.utils.html import format_html


admin.site.register(Country)
admin.site.register(JobPosition)


# @admin.register(JobPosition)
# class JobPositionAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         if object.company.company_logo and hasattr(object.company.company_logo, 'file'):
#             html_code = '<img src = "{}" width = "25px;" style = "border-radius: 50px;"/>'
#             return format_html(html_code.format(object.company.company_logo.url))
#         return "No Image"
    
#     list_display = ('thumbnail','company', 'country', 'title', 'salary_max', 'is_active')
#     list_filter = ('company', 'country', 'is_active', 'experience')
#     search_fields = ('title', 'company', 'address', 'designation')
#     list_display_links = ('title',)
    
    
