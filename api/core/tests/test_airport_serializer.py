from django.test import TestCase
from core.models import Airport, Runway, Flight, Airline
from core.serializers import AirportSerializer
from datetime import datetime

class AirportSerializerTestCase(TestCase):
    def setUp(self):
        self.airport_attributes = {
            'name': "Myrtle Beach International",
            'airport_code': "MYR",
            'address': "1100 Jetport Rd",
            'city': "Myrtle Beach",
            'state': "SC",
            'zip_code': "29577"
        }
        self.dest_attributes = {
            'name': "Atlanta International",
            'airport_code': "ATL",
            'address': "1100 Jetport Rd",
            'city': "Atlanta",
            'state': "GA",
            'zip_code': "12345"
        }
        self.carrier = Airline.objects.create(name="Delta Airlines", airline_code="DL")
        self.airport = Airport.objects.create(**self.airport_attributes)
        self.dest_airport = Airport.objects.create(**self.dest_attributes)
        self.runway1 = Runway.objects.create(airport=self.airport, runway_number=18,
            runway_designation="N", length=5000, width=200)
        self.runway2 = Runway.objects.create(airport=self.airport, runway_number=36,
            runway_designation="N", length=5000, width=200)
        self.flight = Flight.objects.create(
            airline=self.carrier,
            flight_number=123,
            origin=self.airport,
            destination=self.dest_airport,
            departure=datetime(2023, 1, 1, 6, 0),
            arrival=datetime(2023, 1, 1, 9, 0),
            aircraft_type='B747'
        )
        self.serializer = AirportSerializer(instance=self.airport)
        self.serialized_data = self.serializer.data

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'airport_code', 'address', 'city', 'state', 'zip_code', 'runways', 'flight_origin', 'flight_destination']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.airport_attributes['name'])

    def test_airport_code_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['airport_code'], self.airport_attributes['airport_code'])

    def test_address_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['address'], self.airport_attributes['address'])

    def test_city_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['city'], self.airport_attributes['city'])
    
    def test_state_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['state'], self.airport_attributes['state'])

    def test_zip_code_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['zip_code'], self.airport_attributes['zip_code'])

    def test_includes_runways(self):
        self.assertEqual(len(self.serializer.data['runways']), 2)

    def test_airport_departure_data(self):
        data = self.serializer.data
        self.assertTrue(len(data['flight_origin']) > 0)
        self.assertEqual(len(data['flight_destination']), 0)

    def test_airport_arrival_data(self):
        airport_serializer = AirportSerializer(instance=self.dest_airport)
        data = airport_serializer.data
        self.assertTrue(len(data['flight_destination']) > 0)
        self.assertEqual(len(data['flight_origin']), 0)

    def test_create_airport_with_serializer(self):
        serializer = AirportSerializer(data=self.airport_attributes)
        self.assertTrue(serializer.is_valid())
        new_airport = serializer.save()
        self.assertEqual(new_airport.name, self.airport_attributes['name'])

