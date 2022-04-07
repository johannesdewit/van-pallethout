from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('info/', views.info, name='info'),
    path('workshops/', views.workshops, name='workshops'),
    path('projects/', views.projects, name='projects'),
]
