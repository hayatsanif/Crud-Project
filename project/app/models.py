from django.db import models

# Create your models here.
class User(models.Model):
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

class Queryd(models.Model):
    query=models.CharField(max_length=200)
    queryemail=models.CharField(max_length=200)