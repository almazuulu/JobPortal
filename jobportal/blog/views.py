from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from utilities.paginator_page import paginate_queryset
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

topRecentNews = Blog.objects.order_by('-created_at')[:4]
categories = Category.objects.all()

def listblogs(request):
    allNews_list = Blog.objects.all().order_by('-created_at')
    allNews = paginate_queryset(request, allNews_list, 3)
    # pagintor = Paginator(allNews_list, 3) # 3 новости или поста на каждую страницу
    
    # page = request.GET.get('page') # получение номера текущей страницы
    
    # try:
    #     # попытка получение записи для указанной страницы
    #     allNews = pagintor.page(page)
    # except PageNotAnInteger:
    #     # Если страница не явл-ся целым числом, отобразите первую страницу
    #     allNews = pagintor.page(1)
    # except EmptyPage:
    #     # Если страница вне диапазона (например, 9999), отобразить последнюю страницу результатов
    #     allNews = pagintor.page(pagintor.num_pages)
      
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
    
    
