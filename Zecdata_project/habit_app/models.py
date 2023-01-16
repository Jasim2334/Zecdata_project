from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class HabitModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='uploaded_by')
    habit1 = models.CharField(max_length=70,blank=True,)
    habit2 = models.CharField(max_length=70,blank=True,)
    habit3 = models.CharField(max_length=70,blank=True,)
    habit4 = models.CharField(max_length=70,blank=True,)
    habit5 = models.CharField(max_length=70,blank=True,)


# class UserphoneModel(models.Model):
#     phone = models.IntegerField()

