from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Montly_Expenses


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Montly_Expenses_Form(ModelForm):
    class Meta:
        model = Montly_Expenses
        fields = '__all__'

