from django.shortcuts import render
from .models import Blog

def listblogs(request):
    allNews = Blog.objects.all()
    content = {
        'allNews': allNews
    }
    return render(request, 'blog/blogs.html', content)

def blogdetails(request):
    return render(request, 'blog/blog_details.html')
