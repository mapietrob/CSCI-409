"""
Tests for models.
"""

from django.test import TestCase

from core import models

class ModelTests(TestCase):

    def test_create_airport(self):
        """Test Creating an Airport is Successful."""
        airport = models.Airport.objects.create(
            name="Myrtle Beach International",
            airport_code="MYR",
            address="1100 Jetport Rd",
            city="Myrtle Beach",
            state="SC",
            zip_code="29577"
        )

        self.assertEqual(str(airport), airport.name)