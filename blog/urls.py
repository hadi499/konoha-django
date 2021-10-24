from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('create/', views.create, name='blog-create'),
    path('delete/<int:pk>/', views.delete, name='blog-delete'),
    path('detail/<int:pk>/', views.detail, name='blog-detail'),
    path('update/<int:pk>/', views.update, name='blog-update'),
]
