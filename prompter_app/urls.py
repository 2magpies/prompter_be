from django.urls import path, include
from . import views

urlpatterns = [
    path('prompt/', views.prompt_list, name='prompt_list'),
]