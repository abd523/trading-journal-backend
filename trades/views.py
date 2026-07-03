from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # Import AllowAny
from .models import Trade
from .serializers import TradeSerializer

class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    permission_classes = []  # Clear permissions so anyone can add trades locally!

    def get_queryset(self):
        # If the user isn't logged in, just show all trades in our local DB
        if self.request.user.is_anonymous:
            return Trade.objects.all().order_by('-opened_at')
        return Trade.objects.filter(user=self.request.user).order_by('-opened_at')

    def perform_create(self, serializer):
        # If there's no logged-in user, assign it to the first user or leave it empty
        if self.request.user.is_anonymous:
            # We will save it without a user link for easy testing
            serializer.save()
        else:
            serializer.save(user=self.request.user)