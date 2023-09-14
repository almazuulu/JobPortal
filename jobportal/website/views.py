from django.shortcuts import render
from blog.views import topRecentNews

def index(request):
    return render(request, 'website/index.html')


def about(request):
    context = {
        'topRecentNews': topRecentNews,
    }
    return render(request, 'website/about.html', context)

def contact(request):
    return render(request, 'website/contact.html')

def login(request):
    return render(request, 'website/login.html')
