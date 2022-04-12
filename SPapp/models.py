from django.contrib.auth.models import AbstractUser
from django.db import models

class Login(AbstractUser):
    is_student = models.BooleanField(default=False)


class Register_details(models.Model):
    user= models.OneToOneField(Login,on_delete=models.CASCADE,null=True)
    Firstname =models.CharField(max_length=20)
    Lastname =models.CharField(max_length=20)
    emailid =models.EmailField()
    Phone =models.CharField(max_length=10)
    Address1 =models.CharField(max_length=50)
    Address2 =models.CharField(max_length=50)

# # Create your models here.
