from django.test import TestCase
from core.models import Airline
from core.serializers import AirlineSerializer

class AirportSerializerTestCase(TestCase):
    def setUp(self):
        self.airline_attributes = {
            'name': "Delta Airlines",
            'airline_code': "DL"
        }
        self.airline = Airline.objects.create(**self.airline_attributes)
        self.serializer = AirlineSerializer(instance=self.airline)
        self.serialized_data = self.serializer.data

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'airline_code']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.airline_attributes['name'])

    def test_airport_code_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['airline_code'], self.airline_attributes['airline_code'])

    def test_create_airline_with_serializer(self):
        serializer = AirlineSerializer(data=self.airline_attributes)
        self.assertTrue(serializer.is_valid())
        new_airline = serializer.save()
        self.assertEqual(new_airline.name, self.airline_attributes['name'])

