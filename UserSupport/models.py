import profile
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from RBCUSS import settings


# Create your models here.
class Register (AbstractUser,models.Model):
    
    SEX_CHOICES = (('1','Select your gender'),('F', 'Female',),('M', 'Male',),)
    user = settings.AUTH_USER_MODEL
    gender = models.CharField(max_length=1, choices=SEX_CHOICES, default='1')
    birth_date = models.DateField(null=True)
    # profile_image = models.ForeignKey(user,on_delete=models.CASCADE,related_name='user')
    # profile_image= models.ImageField(upload_to='image',blank=True)

    def __str__(self):
        return f'{self.user} Register'

