from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreateionForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta :
        model = get_user_model()
        fields = ('email', 'last_name', 'first_name',)