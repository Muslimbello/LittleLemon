from . import views

from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register("menu", views.MenuViewSet, basename="Menu")
router.register("booking", views.BookingViewSet, basename="Booking")

urlpatterns = [
    path("", include(router.urls)),
    path("message/", views.msg),
    path("login/", obtain_auth_token),
    path("user/", views.UserView.as_view(), name="all-users"),
    path("user-details/", views.UserView_details.as_view(), name="user-info"),
]
