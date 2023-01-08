from rest_framework import routers

from chargepoint.views import ChargePointViewset

base_router = routers.SimpleRouter()
base_router.register(prefix=r'chargepoint', viewset=ChargePointViewset)

urlpatterns = base_router.urls
