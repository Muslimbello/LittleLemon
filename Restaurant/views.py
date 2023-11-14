from django.shortcuts import render, get_object_or_404

from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .serializer import MenuSerializer, BookingSerializer, UserSerializer
from .models import Booking, Menu
from .permissions import IsAdminUserReadOnly
from rest_framework import generics


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUserReadOnly]


class UserView_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUserReadOnly]


@api_view()
@permission_classes([IsAuthenticated])
def homePage(request):
    return render(request, "index.html", {})
