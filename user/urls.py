from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("", views.user_list, name="user_list"),
    path("<int:user_id>/", views.user_detail, name="user_detail"),
    path("edit/<int:user_id>/", views.edit_user, name="edit_user"),
    path("delete/<int:user_id>/", views.delete_user, name="delete_user"),
]
