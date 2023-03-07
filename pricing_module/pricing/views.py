from rest_framework import generics
from .models import ServicesPricing
from .serializers import PricingSerializer

# Create your views here.
class PricingPlanList(generics.ListCreateAPIView):
    queryset = ServicesPricing.objects.all()
    serializer_class = PricingSerializer

class PricingPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicesPricing.objects.all()
    serializer_class = PricingSerializer
