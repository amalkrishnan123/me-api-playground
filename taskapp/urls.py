from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('projects/', views.projects),
    path('search/', views.search),
    path('skills/top/', views.skills_top),
    path('health/', views.health),
]

