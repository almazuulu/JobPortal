from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from utilities.paginator_page import paginate_queryset
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

topRecentNews = Blog.objects.order_by('-created_at')[:4]
categories = Category.objects.all()

def listblogs(request):
    allNews_list = Blog.objects.all().order_by('-created_at')
    allNews = paginate_queryset(request, allNews_list, 3)   
    content = {
        'allNews': allNews,
        'topRecentNews': topRecentNews,
        'categories': categories,
        
    }
    return render(request, 'blog/blogs.html', content)

def blogdetails(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    comments = blog.comments.all()
    context = {
        'blog': blog,
        'topRecentNews': topRecentNews,
        'comments': comments,
        'categories': categories,
    }
    return render(request, 'blog/blog_details.html', context)

def blogs_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news_in_categoryList = Blog.objects.filter(categories=category)
    news_in_category = paginate_queryset(request, news_in_categoryList, 2)
    
    context = {
        'category': category,
        'news_in_category': news_in_category,
        'topRecentNews': topRecentNews,
        'categories': categories,
    }
    
    return render(request, 'blog/blogs_category.html', context)
    
def search_news(request):
    keywords = request.GET.get('keywords')
    
    if not keywords:
        allNews = Blog.objects.all()
    else:
        allNews = Blog.objects.filter(Q(title__icontains=keywords) | Q(content__icontains=keywords))
    
    context = {
        'keywords': keywords,
        'allNews': allNews,
        'topRecentNews': topRecentNews,
        'categories': categories,
    }
    
    return render(request, 'blog/blogs.html', context)
