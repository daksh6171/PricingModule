from rest_framework import serializers
from .models import ServicesPricing

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesPricing
        fields = '__all__'