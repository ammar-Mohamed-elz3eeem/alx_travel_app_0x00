from django.urls import path, include
from rest_framework import routers
from .views import (
    ListingViewSet,
    BookingViewSet,
    ReviewViewSet
)

router = routers.DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls))
]
