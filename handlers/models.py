from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Coupon(models.Model):
    store_name = models.CharField(max_length=200, null= True)
    heading = models.CharField(max_length=200, null= True)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    important_note = models.CharField(max_length=100)
    exp_date = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.heading