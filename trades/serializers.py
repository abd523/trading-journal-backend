from rest_framework import serializers
from .models import Trade

class TradeSerializer(serializers.ModelSerializer):
    pnl = serializers.ReadOnlyField() # Calculated automatically on model save()

    class Meta:
        model = Trade
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}