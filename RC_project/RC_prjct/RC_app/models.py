from django.db import models

# Create your models here.

class Car(models.Model):
   username = models.CharField(max_length=20)
   rent = models.CharField(max_length=10, default=0)
    #capacity = models.CharField(max_length=2)
    # image = models.ImageField(upload_to="")
    # is_available = models.BooleanField(default=True) 

class Customer(models.Model):
    username = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 10)
    

class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    no_of_days = models.CharField(max_length=10,default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # is_complete = models.BooleanField(default=False)
    # rent = models.CharField(max_length=10)

