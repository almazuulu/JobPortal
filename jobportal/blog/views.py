from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

topRecentNews = Blog.objects.order_by('-created_at')[:4]
categories = Category.objects.all()

def listblogs(request):
    allNews = Blog.objects.all()
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
    news_in_category = Blog.objects.filter(categories=category)
    context = {
        'category': category,
        'news_in_category': news_in_category,
        'topRecentNews': topRecentNews,
        'categories': categories,
    }
    
    return render(request, 'blog/blogs_category.html', context)
    
    
