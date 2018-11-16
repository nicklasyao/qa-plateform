from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('user/', views.get_user),
    path('login/', views.log_user_in),
    path('logout/', views.log_user_out),
]