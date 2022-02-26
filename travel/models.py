from django.db import models
from django.conf import settings


class Route(models.Model):
    name = models.CharField(max_length=256, blank=True)

    def __repr__(self):
        return self.name


class FlightStatus:
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    DEPARTED = "departed"

    CHOICES = [
        (SCHEDULED, "scheduled"),
        (CANCELLED, "cancelled"),
        (DEPARTED, "departed"),
    ]


class BookingStatus:
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"

    CHOICES = [
        (SCHEDULED, "scheduled"),
        (CANCELLED, "cancelled"),
    ]


class Flight(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    airline_name = models.CharField(max_length=256, blank=True)
    air_craft_type = models.CharField(max_length=256, blank=True)
    departure = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=30, choices=FlightStatus.CHOICES, default=FlightStatus.SCHEDULED
    )
    route = models.ManyToManyField(
        Route,
        db_table="flight_routes",
        related_name="routes",
        related_query_name="route",
    )
    flight_number = models.CharField(max_length=30, blank=True)
    number_of_seats = models.PositiveIntegerField(blank=True, null=True)

    def __repr__(self):
        pass


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    flight = models.ForeignKey(
        Flight,
        blank=True,
        null=True,
        related_name="bookings",
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="bookings",
        on_delete=models.SET_NULL,
    )
    status = models.CharField(
        max_length=30, choices=BookingStatus.CHOICES, default=BookingStatus.SCHEDULED
    )

    def __repr__(self):
        pass
