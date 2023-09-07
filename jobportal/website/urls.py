from django.urls import path, include
from .views import index, about, contact, login, alljobs

urlpatterns = [
    path("", index, name='home'),
    path("jobs/", alljobs, name='jobs'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("login/", login, name='login'),
]
