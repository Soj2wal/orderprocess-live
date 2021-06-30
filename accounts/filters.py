from .models import *
from django.db.models import fields
from django.forms import widgets
from django import forms
import django_filters
from django_filters import CharFilter


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'category', 'price']


class CustomerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    phone = CharFilter(field_name='phone', lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['name', 'phone']


class CustomerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    phone = CharFilter(field_name='phone', lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['name', 'phone']


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['customer', 'status']


class StaffFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Staff
        fields = ['name', 'position']
