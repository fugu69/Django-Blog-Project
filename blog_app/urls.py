from django.urls import path
from . import views

urlpatterns = [
    # leads to the function home from views folder to handle the request
    # (*project urls* -> app urls -> function -> response)
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]