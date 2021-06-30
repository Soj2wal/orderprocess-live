from django.forms import ModelForm, fields, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'tags', 'price']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'name', 'phone', 'email', 'address',
                  'increment_rate', 'salary', 'position', 'profile_pic']
        exclude = ['user']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address', 'email']
