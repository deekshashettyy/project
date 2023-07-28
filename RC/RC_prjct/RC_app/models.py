from django.db import models

# Create your models here.

class Car(models.Model):
   car_name = models.CharField(max_length=20)
   no_of_days = models.CharField(max_length=3) 

class Customer(models.Model):
    username = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 10)
    

class Order(models.Model):
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rent = models.ForeignKey(Car, on_delete=models.CASCADE)
   