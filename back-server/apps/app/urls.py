from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('logout/', views.log_user_out),
    path('logging/', views.logging_in),
]