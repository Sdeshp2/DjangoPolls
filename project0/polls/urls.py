from django.contrib import admin
from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path("", views.index,name='index'),
    path("about/",views.about,name='about'),
    path('<int:question_id>/', views.detail, name='detail'),
  
    
]
