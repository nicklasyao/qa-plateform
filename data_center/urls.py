from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_home),
    path('province/', views.get_province),
    path('house/add', views.add_house),
]