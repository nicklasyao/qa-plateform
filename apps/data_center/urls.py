from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_home),
    path('province/', views.get_province),
    path('house/add', views.add_house),
    path('pointsale/add', views.add_point_sale),
    path('payinfo/add', views.add_pay_info),
    path('customer/add', views.add_customer),
    path('approve/add', views.auto_approve),
]