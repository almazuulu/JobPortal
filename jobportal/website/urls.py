from django.urls import path
from .views import index, about, contact, login

urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("login/", login, name='login'),
]
