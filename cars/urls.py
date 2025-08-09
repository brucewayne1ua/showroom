from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('add/', views.car_add, name='car_add'),
    path('<int:pk>/', views.car_detail, name='car_detail'),
]