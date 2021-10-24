from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AuthenticationRememberMeForm(AuthenticationForm):

    """
    Subclass of Django ``AuthenticationForm`` which adds a remember me
    checkbox.

    """

    remember_me = forms.BooleanField(label=('Remember Me'), initial=False,
                                     required=False)
