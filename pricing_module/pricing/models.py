from django.db import models

# Create your models here.

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DistanceBasePrice(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    distance_in_km = models.DecimalField(max_digits=5, decimal_places=2)
    base_price = models.DecimalField(max_digits=8, decimal_places=2)

class DistanceAdditionalPrice(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    price_per_km = models.DecimalField(max_digits=8, decimal_places=2)

class TimeMultiplierFactor(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    time_in_minutes = models.IntegerField()
    multiplier_factor = models.DecimalField(max_digits=5, decimal_places=2)