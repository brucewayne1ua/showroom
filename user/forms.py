from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number"]

class PhoneAuthForm(AuthenticationForm):
    username = forms.CharField(label="Phone number")
