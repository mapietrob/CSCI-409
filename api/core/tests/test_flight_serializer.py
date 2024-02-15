from django.test import TestCase
from core.models import Airport, Flight, Airline
from core.serializers import FlightSerializer
from datetime import datetime

class FlightSerializerTestCase(TestCase):
    def setUp(self):
        self.current_time = datetime.now()
        self.carrier = Airline.objects.create(name="Delta Airlines", airline_code="DL")
        self.origin = Airport.objects.create(name="AP1", airport_code="ABC", address="123 Any Street", city="Any Town", state="SC", zip_code="12345")
        self.dest = Airport.objects.create(name="AP2", airport_code="DEF", address="456 Any Street", city="Any Town", state="GA", zip_code="23456")
        self.flight_data = {
            'origin':self.origin,
            'destination':self.dest,
            'airline':self.carrier,
            'flight_number':1954,
            'departure':self.current_time,
            'arrival':self.current_time,
            'aircraft_type':'B747',
        }
        self.flight = Flight.objects.create(**self.flight_data)
        self.serializer = FlightSerializer(instance=self.flight)
        self.serialized_data = self.serializer.data

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['origin', 'destination', 'airline', 'flight_number', 'departure', 'arrival', 'aircraft_type']))

    def test_origin_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.origin, self.flight_data['origin'])

    def test_destination_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.dest, self.flight_data['destination'])

    def test_airline_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.carrier, self.flight_data['airline'])

    def test_flight_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['flight_number'], self.flight_data['flight_number'])

    def test_aircraft_type_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['aircraft_type'], self.flight_data['aircraft_type'])

    def test_arrival_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.current_time, self.flight_data['arrival'])

    def test_departure_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.current_time, self.flight_data['departure'])

    def test_create_flight_with_serializer(self):
        # A serializer requires the id of the foreign key relation to be added instead of an instance of the object
        #    Override airport to the id of the airport
        self.flight_data['origin'] = self.origin.id
        self.flight_data['destination'] = self.dest.id
        self.flight_data['airline'] = self.carrier.id
        serializer = FlightSerializer(data=self.flight_data)
        self.assertTrue(serializer.is_valid()) # Checks that the serializer is valid
        new_flight = serializer.save()
        self.assertEqual(new_flight.flight_number, self.flight_data['flight_number'])


