from rest_framework import serializers
from .models import Exchange, ExchangeAccount

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'

class ExchangeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeAccount
        fields = ('id', 'exchange', 'account_name', 'api_key', 'api_secret', 'is_valid', 'created_at')
        extra_kwargs = {'api_secret': {'write_only': True}} # Never expose secrets via GET requests!