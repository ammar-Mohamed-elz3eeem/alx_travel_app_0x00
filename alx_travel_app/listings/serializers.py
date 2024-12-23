from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    booking_id = serializers.HyperlinkedIdentityField(view_name='booking-detail')

    class Meta:
        model = Booking
        fields = ('url', 'booking_id', 'listing_id', 'user_id', 'start_date', 'end_date', 'total_price')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    review_id = serializers.HyperlinkedIdentityField(view_name='review-detail')

    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    host_id = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())

    class Meta:
        model = Listing
        fields = ('name', 'host_id', 'description', 'location', 'pricepernight', 'listing_reviews', 'listing_bookings')
