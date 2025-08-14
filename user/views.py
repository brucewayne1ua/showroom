from django.shortcuts import render, get_object_or_404, redirect
from user.models import User
from .forms import UserForm
from django.contrib import messages
from django import forms

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # <- обязательно сохранить в переменную!
            messages.success(request, "User registered successfully!")
            return redirect('user_detail', user_id=user.id)  # теперь user доступен
    else:
        form = UserForm()
    return render(request, 'users/user_register.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully!")
            return redirect('user_list')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'users/edit_user.html', {'form': form, 'user': user})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('user_list')
    return render(request, 'users/delete_user.html', {'user': user})

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'users/user_detail.html', {'user': user})