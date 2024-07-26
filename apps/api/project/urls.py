from django.urls import path
from .views import *

urlpatterns = [
    path('create_project', create_react_project, name='create_project'),
    path('create-django-project/', create_django_project, name='create_django_project'),
    path('create-springboot-project/', create_springboot_project, name='create_springboot_project'),
    path('create-angular-project/', create_angular_project, name='create_angular_project'),
]
