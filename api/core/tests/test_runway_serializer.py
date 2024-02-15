from django.test import TestCase
from core.models import Airport, Runway
from core.serializers import RunwaySerializer

class RunwaySerializerTestCase(TestCase):
    def setUp(self):
        self.airport = Airport.objects.create(
            name="Myrtle Beach International",
            airport_code="MYR",
            address="1100 Jetport Rd",
            city="Myrtle Beach",
            state="SC",
            zip_code="29577"
        )
        self.runway_attributes = {
            'airport': self.airport,
            'runway_number': 18,
            'runway_designation': "N",
            'length': 5000,
            'width': 5000
        }
        self.runway = Runway.objects.create(**self.runway_attributes)
        self.serializer = RunwaySerializer(instance=self.runway)
        self.serialized_data = self.serializer.data

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['airport', 'runway_number', 'runway_designation', 'length', 'width']))

    def test_runway_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['runway_number'], self.runway_attributes['runway_number'])

    def test_runway_designation_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['runway_designation'], self.runway_attributes['runway_designation'])

    def test_length_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['length'], self.runway_attributes['length'])

    def test_width_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['width'], self.runway_attributes['width'])

    def test_airport_field_content(self):
        data = self.serializer.data
        self.assertEqual(self.airport, self.runway_attributes['airport'])

    def test_create_runway_with_serializer(self):
        # A serializer requires the id of the foreign key relation to be added instead of an instance of the object
        #    Override airport to the id of the airport
        self.runway_attributes['airport'] = self.airport.id
        serializer = RunwaySerializer(data=self.runway_attributes)
        self.assertTrue(serializer.is_valid()) # Checks that the serializer is valid
        new_runway = serializer.save()
        self.assertEqual(new_runway.runway_number, self.runway_attributes['runway_number'])

