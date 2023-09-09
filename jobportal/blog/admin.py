from django.contrib import admin
from .models import Blog, Category, Comment
from django.utils.html import format_html

admin.site.register(Category)
admin.site.register(Comment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if object.image and hasattr(object.image, 'file'):
            html_code = '<img src = "{}" width = "40" style = "border-radius: 50px;"/>'
            return format_html(html_code.format(object.image.url))
        return "No Image"
    
    
    list_display = ('thumbnail', 'author', 'title', 'created_at')
    list_filter = ('categories', 'title')
    search_fields = ('author','title')
    list_display_links = ('author', 'title',)


