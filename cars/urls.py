from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("", views.car_list, name="car_list"),
    path("filter/", views.car_filter, name="car_filter"),
    path("<int:pk>/", views.car_detail, name="car_detail"),
    path("add/", views.car_add, name="car_add"),
    path("buy/<int:pk>/", views.car_buy, name="car_buy"),
    path("thanks/", views.order_thanks, name="order_thanks"),
    path("my-cars/", views.my_cars, name="my_cars"),
    
]
