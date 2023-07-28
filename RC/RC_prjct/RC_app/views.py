from django.shortcuts import render, redirect
from .models import Customer
from .models import Car
from .models import Order
# Create your views here.

def RC_home (req):

    if req.method =="POST":
        name_1 = req.POST["name"]
        phone_1 = req.POST["phone"]

        obj = Customer(username=name_1, phone=phone_1)
        obj.save()
        return redirect('/RC/all_cars')
    else:
        return render(req, "RC_app/index.html") 
    

def all_cars(req):

    if req.method =="POST":
        car = req.POST["Car_name"]
        days_1=req.POST["days"]

        obj = Car(car_name=car, no_of_days=days_1)
        obj.save()
        return redirect('/RC/order_details')
    else:
        return render(req, "RC_app/cars_list.html") 
    

def order_details(req):

    cust = Customer.objects.all()
    content = {"user_details" : cust}
    return render(req, "RC_app/summary.html",content) 
