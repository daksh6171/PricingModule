from django import forms
from .models import (
    PricingConfig,
    DistanceBasePrice,
    DistanceAdditionalPrice,
    TimeMultiplierFactor,
    Users,
)

class PricingConfigForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    is_enabled = forms.BooleanField(required=True)

    class Meta:
        model = PricingConfig
        fields = '__all__'

class DistanceBasePriceForm(forms.ModelForm):
    class Meta:
        model = DistanceBasePrice
        fields = '__all__'

class DistanceAdditionalPriceForm(forms.ModelForm):
    class Meta:
        model = DistanceAdditionalPrice
        fields = '__all__'
    
class TimeMultiplierFactorForm(forms.ModelForm):
    class Meta:
        model = TimeMultiplierFactor
        fields = '__all__'

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'