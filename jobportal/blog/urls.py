from django.urls import path, include
from .views import listblogs, blogdetails

urlpatterns = [
    path('', listblogs, name='blogs'), #website.com/blog/,
    path('<str:blog_id>', blogdetails, name='blog_details'), #website.com/blog/adsasd3we23432432424rewfwe-sdfsdf
]