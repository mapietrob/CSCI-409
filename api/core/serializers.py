from rest_framework import serializers 
from core.models import Airline, Airport, Runway, Flight 

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ('id', 'name', 'airports', 'runway_number', 'length', 'width')
        read_only_fields = ('id',)