from django.contrib import admin
from .models import Blog
from django.utils.html import format_html

# admin.site.register(Blog)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        html_code = '<img src = "{}" width = "40" style = "border-radius: 50px;"/>'
        return format_html(html_code.format(object.image.url))
    
    
    list_display = ('thumbnail', 'author', 'title', 'created_at')
    list_filter = ('author', 'title')
    search_fields = ('author','title')
    list_display_links = ('author', 'title',)


