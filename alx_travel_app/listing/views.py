from django.shortcuts import render
from rest_framework.viewsets import generics, GenericViewSet
from rest_framework import permissions
from .serializers import ListingSerializer
from .models import Listing


class ListingViewSet(GenericViewSet, generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.AllowAny,)
