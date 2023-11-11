from django.shortcuts import render

from .models import Booking, Menu
from .serializer import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
class MenuViewSet(viewsets.ModelViewSet):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]