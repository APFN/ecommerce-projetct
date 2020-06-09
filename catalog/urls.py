from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.product_list, name= 'product_list'),
    re_path('(?P<slug>[\w_-]+)/', views.category, name= 'category'),
] 