from django import forms 
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CouponForm(ModelForm): 
    class Meta:
        model = Coupon
        fields = '__all__'