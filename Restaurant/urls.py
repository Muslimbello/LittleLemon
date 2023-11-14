from . import views

from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register("menu", views.MenuViewSet, basename="Menu")
router.register("booking", views.BookingViewSet, basename="Booking")
router.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/login/", obtain_auth_token),
    path("home/", views.homePage, name="home"),
]
