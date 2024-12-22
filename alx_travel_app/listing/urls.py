from django.urls import path, include
from rest_framework import routers
from .views import (
    ListingViewSet,
    BookingViewSet,
    ReviewViewSet
)

router = routers.DefaultRouter()
router.register(r'listings/', ListingViewSet, basename='listing'),
router.register(r'booking/', BookingViewSet, basename='booking'),
router.register(r'reviews/', ReviewViewSet, basename='review'),

urlpatterns = [
    path('', include(router.urls))
]
