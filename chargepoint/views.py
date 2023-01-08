# Django apps imports
from django.shortcuts import render

# Third party apps imports
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# Local apps imports
from chargepoint.models import ChargePoint
from chargepoint.serializers import ChargePointSerializer, ChargePointUpdateSerializer, ChargePointCreateSerializer


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]['Default']
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()

class ChargePointViewset(MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    model_class = ChargePoint
    serializer_class = ChargePointSerializer
    queryset = ChargePoint.objects.all()
    serializer_action_classes = {
        'list': {'Default': ChargePointSerializer},
        'update': {'Default': ChargePointUpdateSerializer},
        'retrieve': {'Default': ChargePointSerializer},
        'create': {'Default': ChargePointCreateSerializer},
    }
    permission_classes = [AllowAny]


