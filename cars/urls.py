from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.car_list, name='car_list'),              
    path('add/', views.car_add, name='car_add'),        
    path('order-thanks/', views.order_thanks, name='order_thanks'),
    path('<int:pk>/', views.car_detail, name='car_detail'), 
     path('<int:pk>/buy/', views.car_buy, name='car_buy'),
]
