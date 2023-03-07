from django.urls import path
from rest_framework import routers
from . import views
# from views import CalculatePricingView


router = routers.SimpleRouter()
# router.register(r'pricing-config', PricingConfigView, basename='pricing-config')

urlpatterns = [
    path('pricing-config/', views.PricingConfigListCreateView.as_view(), name='pricing-config-list'),
    path('pricing-config/<int:pk>/', views.PricingConfigDetailView.as_view(), name='pricing-config-detail'),
    path('distance-base-price/', views.DistanceBasePriceListCreateView.as_view(), name='distance-base-price-list'),
    path('distance-base-price/<int:pk>/', views.DistanceBasePriceDetailView.as_view(), name='distance-base-price-detail'),
    path('distance-additional-price/', views.DistanceAdditionalPriceListCreateView.as_view(), name='distance-additional-price-list'),
    path('distance-additional-price/<int:pk>/', views.DistanceAdditionalPriceDetailView.as_view(), name='distance-additional-price-detail'),
    path('time-multiplier-factor/', views.TimeMultiplierFactorListCreateView.as_view(), name='time-multiplier-factor-list'),
    path('time-multiplier-factor/<int:pk>/', views.TimeMultiplierFactorDetailView.as_view(), name='time-multiplier-factor-detail'),
    path('calculate-pricing/', views.CalculatePricingView.as_view(), name='calculate-pricing'),
]
