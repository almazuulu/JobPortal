from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about, contact, login, alljobs

urlpatterns = [
    path("", index, name='home'),
    path("jobs/", alljobs, name='jobs'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("login/", login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 