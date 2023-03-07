from django.contrib import admin
from django.urls import include, path
from .views import PricingPlanDetail, PricingPlanList

urlpatterns = [
    path('pricing_plans/', PricingPlanList.as_view(), name = 'pricing_plan_list'),
    path('pricing_plans/<int:pk>/', PricingPlanDetail.as_view(), name= 'pricing_plan_details'),
]