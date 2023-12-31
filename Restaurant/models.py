from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    Title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.Title


class Booking(models.Model):
    name = models.CharField(max_length=225)
    no_of_guests = models.IntegerField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
