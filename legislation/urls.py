from django.urls import path
from . import views

urlpatterns = [
    path('', views.law_list, name='law_list'),
    path('law/<int:pk>/', views.law_detail, name='law_detail'),
]
