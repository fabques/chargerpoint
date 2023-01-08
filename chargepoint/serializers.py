from rest_framework import serializers

from chargepoint.models import ChargePoint


class ChargePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargePoint
        fields = '__all__'

class ChargePointUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargePoint
        fields = ['status']

class ChargePointCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargePoint
        fields = ['name', 'status']
