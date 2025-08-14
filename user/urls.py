from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # /users/
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('<int:user_id>/', views.user_detail, name='user_detail'),  # /users/10/
]
