# Django apps imports
from django.shortcuts import render

# Third party apps imports
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# Local apps imports
from chargepoint.models import ChargePoint
from chargepoint.serializers import ChargePointSerializer


class ChargePointViewset(viewsets.ModelViewSet):
    model_class = ChargePoint
    serializer_class = ChargePointSerializer
    queryset = ChargePoint.objects.all()
    serializer_action_classes = {
        'list': {'Staff': ChargePointSerializer, 'Default': ChargePointSerializer},
    }
    # filter_backends = [ChargePointStatusFilter, DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    # filterset_fields = []
    # search_fields = []
    # ordering = ['id_user__first_name']


