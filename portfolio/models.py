from django.db import models
from django.conf import settings
from exchanges.models import ExchangeAccount

class Balance(models.Model):
    WALLET_CHOICES = [('SPOT', 'Spot'), ('FUTURES', 'Futures/Derivatives')]
    exchange_account = models.ForeignKey(ExchangeAccount, on_delete=models.CASCADE, related_name='balances')
    asset = models.CharField(max_length=20)
    wallet_type = models.CharField(max_length=10, choices=WALLET_CHOICES, default='SPOT')
    amount = models.DecimalField(max_digits=30, decimal_places=10)
    usd_value = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('exchange_account', 'asset', 'wallet_type')