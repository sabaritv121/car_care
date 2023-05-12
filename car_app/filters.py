from django import forms

from car_app.models import Login
import django_filters
from django_filters import CharFilter,filters



class UserFilter(django_filters.FilterSet):
    name = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search ', 'class': 'form-control'}))

    class Meta:
        model = Login
        fields = ('name',)