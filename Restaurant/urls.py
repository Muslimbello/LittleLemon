
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('menu', views.MenuViewSet , basename='Menu')
router.register('booking', views.BookingViewSet, basename='Booking')

urlpatterns = [
	path('', include(router.urls)),
]