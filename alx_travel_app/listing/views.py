from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import (
    ListingSerializer,
    BookingSerializer,
    ReviewSerializer
)
from .models import Listing, Booking, Review


class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.AllowAny,)


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.AllowAny,)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.AllowAny,)
