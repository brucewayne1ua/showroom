from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import User
from .forms import UserForm, UserUpdateForm

def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, "User registered and logged in successfully!")
            return redirect("user_detail", user_id=user.id)
    else:
        form = UserForm()
    return render(request, "users/user_register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("user_list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login_user")



@login_required(login_url="login_user")
def user_list(request):
    users = User.objects.all()
    return render(request, "users/user_list.html", {"users": users})



@login_required(login_url="login_user")
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "users/user_detail.html", {"user": user})



@login_required(login_url="login_user")
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect("user_list")
    else:
        form = UserUpdateForm(instance=user)
    return render(request, "users/edit_user.html", {"form": form, "user": user})



@login_required(login_url="login_user")
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect("user_list")
    return render(request, "users/delete_user.html", {"user": user})
