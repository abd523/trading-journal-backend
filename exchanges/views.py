from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exchange, ExchangeAccount
from .serializers import ExchangeSerializer, ExchangeAccountSerializer

class ExchangeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    permission_classes = [IsAuthenticated]

class ExchangeAccountViewSet(viewsets.ModelViewSet):
    serializer_class = ExchangeAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExchangeAccount.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)