from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def alljobs(request):
    context = {
        'titlepage': 'All jobs'
    }
    return render(request, 'website/jobs.html', context)

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def login(request):
    return render(request, 'website/login.html')
