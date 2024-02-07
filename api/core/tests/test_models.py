"""
Tests for models.
"""

from django.test import TestCase
from core import models
from datetime import datetime, timedelta

def create_airport():
    """Helper function to create a sample airport."""
    return models.Airport.objects.create(
        name="Myrtle Beach International",
        airport_code="MYR",
        address="1100 Jetport Rd",
        city="Myrtle Beach",
        state="SC",
        zip_code="29577"
    )

class ModelTests(TestCase):

    def test_create_airport(self):
        """Test creating an airport is successful."""
        airport = create_airport()

        self.assertEqual(str(airport), airport.name)

    def test_create_airline(self):
        """Test creating an airline is successful."""
        airline = models.Airline.objects.create(
            name="Delta Airlines",
            airline_code="DL"
        )

        self.assertEqual(str(airline), airline.name)

    def test_create_runway(self):
        """Test creating a runway is successful."""
        airport = create_airport()
        runway = models.Runway.objects.create(
            airport=airport,
            runway_number=18,
            runway_designation="N",
            length=5000,
            width=5000
        )

        self.assertEqual(str(runway), f"{runway.runway_number}{runway.runway_designation}")

    def test_create_flight(self):
        """Test creating a flight is successful."""
        origin_airport = create_airport()
        destination_airport = models.Airport.objects.create(
            name="Los Angeles International",
            airport_code="LAX",
            address="1 World Way",
            city="Los Angeles",
            state="CA",
            zip_code="90045"
        )
        airline = models.Airline.objects.create(
            name="Delta Airlines",
            airline_code="DL"
        )
        flight = models.Flight.objects.create(
            origin=origin_airport,
            destination=destination_airport,
            airline=airline,
            flight_number=1954,
            departure=datetime.now(),
            arrival=datetime.now() + timedelta(hours=5),
            aircraft_type="B747"
        )

        self.assertEqual(str(flight), f"{flight.airline.airline_code}{flight.flight_number}")
