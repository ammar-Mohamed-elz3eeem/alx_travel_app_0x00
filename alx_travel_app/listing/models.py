import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core import validators


class Listing(models.Model):
    """
    This class represents single listing object from the listings table
    """
    listing_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    host_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=False)
    location = models.CharField(max_length=255, blank=False)
    pricepernight = models.DecimalField(decimal_places=2, max_digits=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    """
    This class represents single booking object from the bookings table
    """
    STATUS_CHOICES = (
        ('PENDING', 'pending'),
        ('CONFIRMED', 'confirmed'),
        ('CANCELED', 'canceled'),
    )
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    listing_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listing_bookings')
    user_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='user_bookings')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_price = models.DecimalField(decimal_places=2, max_digits=7)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    """
    This class represents single review object from the reviews table
    """
    STATUS_CHOICES = (
        ('PENDING', 'pending'),
        ('CONFIRMED', 'confirmed'),
        ('CANCELED', 'canceled'),
    )
    review_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    listing_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    user_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='listing_reviews')
    rating = models.IntegerField(validators=(validators.MinValueValidator, validators.MaxValueValidator))
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
