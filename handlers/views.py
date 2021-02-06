from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Coupon
from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def coupons(request):
    return render(request, 'coupons.html')

def addcoupon(request):
    context = {}
    if request.method == "POST":
        form = CouponForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = Coupon()
            
            post.store_name = form.cleaned_data.get("store_name")
            post.heading = form.cleaned_data.get("heading")
            post.code = form.cleaned_data.get("code")
            post.description = form.cleaned_data.get("description")
            post.important_note = form.cleaned_data.get("important_note")
            post.exp_date = form.cleaned_data.get("exp_date")
            post.owner = form.cleaned_data.get("owner")
            
            post.save()
            context['form']= form
            return render(request, 'coupons.html', context)
        
    else:
        form = CouponForm()
        context['form']= form
        return render(request, 'addcoupon.html', context)
    