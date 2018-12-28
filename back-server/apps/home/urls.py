from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('user/', views.get_user),
    path('login1/', views.log_user_in),
    path('logout1/', views.log_user_out),
#    rest
    path('logging/', views.logging_in),
]