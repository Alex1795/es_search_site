from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('query', views.search_page, name='search_page'),
]