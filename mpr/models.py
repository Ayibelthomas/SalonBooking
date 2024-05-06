from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Login(models.Model):
    user_type=models.CharField(max_length=30)
    view_password=models.CharField(max_length=50)
    view_email=models.CharField(max_length=50)
    is_active =models.CharField(max_length=30,null =True)

    
class User(models.Model):
    user= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=20)
    Email=models.EmailField()
    Phonenumber=models.IntegerField()
    Password=models.CharField(max_length=20)
    Image=models.FileField(null= True)
    Address=models.CharField(max_length=200)
    status=models.CharField(max_length=20,default='pending')


class Employee(models.Model):
    employee= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username1=models.CharField(max_length=20)
    Email1=models.EmailField()
    Phonenumber1=models.IntegerField()
    Password1=models.CharField(max_length=20)
    Image1=models.FileField(null= True)
    Address1=models.CharField(max_length=200)
    status=models.CharField(max_length=20,default='pending')


class Request(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    employee= models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    Datetime=models.DateField(null=True)
    Phone =models.IntegerField(max_length=10,null=True)
    Price=models.IntegerField(null=True)
    Time = models.TimeField()
    am_pm = models.CharField(max_length=2,null=True)
    Service = models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=20,default='pending')

class Payment(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')