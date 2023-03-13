from django.contrib import admin
from .models import (
    PricingConfig,
    DistanceBasePrice,
    DistanceAdditionalPrice,
    TimeMultiplierFactor,
    Users,
)

from .forms import PricingConfigForm, DistanceBasePriceForm, DistanceAdditionalPriceForm, TimeMultiplierFactorForm, UsersForm
# Register your models here.

class PricingConfigAdmin(admin.ModelAdmin):
    form = PricingConfigForm

class DistanceBasePriceAdmin(admin.ModelAdmin):
    form = DistanceBasePriceForm

class DistanceAdditionalPriceAdmin(admin.ModelAdmin):
    form = DistanceAdditionalPriceForm

class TimeMultiplierFactorAdmin(admin.ModelAdmin):
    form = TimeMultiplierFactorForm

class UsersAdmin(admin.ModelAdmin):
    form = UsersForm



admin.site.register(PricingConfig, PricingConfigAdmin)
admin.site.register(DistanceBasePrice, DistanceBasePriceAdmin)
admin.site.register(DistanceAdditionalPrice, DistanceAdditionalPriceAdmin)
admin.site.register(TimeMultiplierFactor, TimeMultiplierFactorAdmin)
admin.site.register(Users, UsersAdmin)
