import decimal
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .models import PricingConfig, DistanceBasePrice, DistanceAdditionalPrice, TimeMultiplierFactor

from .serializers import (
    PricingConfigSerializer, DistanceBasePriceSerializer,
    DistanceAdditionalPriceSerializer, TimeMultiplierFactorSerializer
)

class PricingConfigListCreateView(generics.ListCreateAPIView):
    queryset = PricingConfig.objects.all()
    serializer_class = PricingConfigSerializer


class PricingConfigDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PricingConfig.objects.all()
    serializer_class = PricingConfigSerializer


class DistanceBasePriceListCreateView(generics.ListCreateAPIView):
    # queryset = DistanceBasePrice.objects.all()
    serializer_class = DistanceBasePriceSerializer

    def get_queryset(self):
        pricing_id = self.request.data.get('pricin_config')
        pricing_config = PricingConfig.objects.get(id=pricing_id)
        print(pricing_config)
        # queryset = DistanceBasePrice.objects.all()
        # pricing_config_id = self.request.data.get('pricing-config')
        # pricing_config_id = self.request.query_params.get('pricing_config_id', None)
        if not pricing_config:
            return Response({'error':'pricing config id mismatch'}, status=status.HTTP_204_NO_CONTENT)
        else:
            queryset = DistanceBasePrice.objects.all()
        return queryset


class DistanceBasePriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DistanceBasePrice.objects.all()
    serializer_class = DistanceBasePriceSerializer


class DistanceAdditionalPriceListCreateView(generics.ListCreateAPIView):
    serializer_class = DistanceAdditionalPriceSerializer

    def get_queryset(self):
        pricing_id = self.request.data.get('pricing_config')
        pricing_config = PricingConfig.objects.get(id=pricing_id)
        print(pricing_config)
        # queryset = DistanceBasePrice.objects.all()
        # pricing_config_id = self.request.data.get('pricing-config')
        # pricing_config_id = self.request.query_params.get('pricing_config_id', None)
        if not pricing_config:
            return Response({'error':'pricing config id mismatch'}, status=status.HTTP_204_NO_CONTENT)
        else:
            queryset = DistanceAdditionalPrice.objects.all()
        return queryset


class DistanceAdditionalPriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DistanceAdditionalPrice.objects.all()
    serializer_class = DistanceAdditionalPriceSerializer


class TimeMultiplierFactorListCreateView(generics.ListCreateAPIView):
    serializer_class = TimeMultiplierFactorSerializer

    def get_queryset(self):
        pricing_id = self.request.data.get('pricing_config')
        pricing_config = PricingConfig.objects.get(id=pricing_id)
        print(pricing_config)
        # queryset = DistanceBasePrice.objects.all()
        # pricing_config_id = self.request.data.get('pricing-config')
        # pricing_config_id = self.request.query_params.get('pricing_config_id', None)
        if not pricing_config:
            return Response({'error':'pricing config id mismatch'}, status=status.HTTP_204_NO_CONTENT)
        else:
            queryset = TimeMultiplierFactor.objects.all()
        return queryset


class TimeMultiplierFactorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeMultiplierFactor.objects.all()
    serializer_class = TimeMultiplierFactorSerializer


class CalculatePricingView(APIView):
    def post(self, request):
        try:
            # Get distance and time from request data
            distance = decimal.Decimal(request.data.get('distance', 0))
            time = int(request.data.get('time', 0))
            time_in_min = time*60

            # Find the currently enabled pricing configuration
            pricing_config = PricingConfig.objects.filter(is_enabled=True).first()
            if not pricing_config:
                return Response({'error': 'No pricing configuration enabled'}, status=status.HTTP_400_BAD_REQUEST)

            # Calculate distance-based price
            dbp = DistanceBasePrice.objects.filter(pricing_config=pricing_config, distance_in_km__lte=distance).order_by('distance_in_km').first()
            if not dbp:
                return Response({'error': 'Invalid distance'}, status=status.HTTP_400_BAD_REQUEST)

            # Calculate additional price
            dap = DistanceAdditionalPrice.objects.filter(pricing_config=pricing_config).first()
            if not dap:
                return Response({'error': 'No additional price found'}, status=status.HTTP_400_BAD_REQUEST)
            additional_price = (distance - dbp.distance_in_km) * dap.price_per_km

            # Calculate time multiplier factor
            tmf = TimeMultiplierFactor.objects.filter(pricing_config=pricing_config, time_in_minutes__gte=time_in_min).order_by('time_in_minutes').first()
            if not tmf:
                return Response({'error': 'Invalid time'}, status=status.HTTP_400_BAD_REQUEST)

            # Calculate final price
            price = (dbp.base_price + additional_price) * tmf.multiplier_factor

            return Response({'price': price}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
