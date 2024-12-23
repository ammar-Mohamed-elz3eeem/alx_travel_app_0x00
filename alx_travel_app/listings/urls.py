from django.urls import path, include
from rest_framework import routers
from .views import (
    ListingViewSet,
    BookingViewSet,
    ReviewViewSet,
    UserViewSet
)

router = routers.DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]
