from django.urls import path
from .views import RC_home
from .views import all_cars
from . import views

urlpatterns = [
    path('home/', RC_home),
    path("all_cars/", views.all_cars, name="all_cars"),
    path("order_details/", views.order_details, name="order_details"),
]