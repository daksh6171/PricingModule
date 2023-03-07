from rest_framework import serializers
from .models import PricingConfig, DistanceBasePrice, DistanceAdditionalPrice, TimeMultiplierFactor

class DistanceBasePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistanceBasePrice
        fields = '__all__'

class DistanceAdditionalPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistanceAdditionalPrice
        fields = '__all__'

class TimeMultiplierFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeMultiplierFactor
        fields = '__all__'

class PricingConfigSerializer(serializers.ModelSerializer):
    distance_base_prices = DistanceBasePriceSerializer(many=True, read_only=True)
    distance_additional_prices = DistanceAdditionalPriceSerializer(many=True, read_only=True)
    time_multiplier_factors = TimeMultiplierFactorSerializer(many=True, read_only=True)

    class Meta:
        model = PricingConfig
        fields = ('id', 'name', 'is_enabled', 'distance_base_prices', 'distance_additional_prices', 'time_multiplier_factors')
