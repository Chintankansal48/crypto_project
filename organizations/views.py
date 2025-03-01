from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organization, CryptoPrice
from .serializers import OrganizationSerializer, CryptoPriceSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

class CryptoPriceViewSet(viewsets.ModelViewSet):
    queryset = CryptoPrice.objects.all()
    serializer_class = CryptoPriceSerializer
    permission_classes = [IsAuthenticated]
