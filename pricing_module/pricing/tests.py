import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import PricingConfig


class CreatePricingConfigTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("pricing-config-list")
        self.payload = {"name": "Test Pricing Config", "is_enabled": True}

    def test_create_pricing_config_success(self):
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PricingConfig.objects.count(), 1)
        self.assertEqual(PricingConfig.objects.first().name, "Test Pricing Config")
        self.assertEqual(PricingConfig.objects.first().is_enabled, True)

    def test_create_pricing_config_invalid_payload(self):
        # Sending a payload without a name field
        invalid_payload = {"is_enabled": True}
        response = self.client.post(self.url, invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PricingConfig.objects.count(), 0)
