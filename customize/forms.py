from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('display_name', 'homepage', 'age')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('display_name', 'homepage', 'age')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=50)
    homepage = forms.URLField(max_length=50, required=False)
    age = forms.IntegerField()