from django.db import models
from django.conf import settings
from exchanges.models import ExchangeAccount

class Trade(models.Model):
    SIDE_CHOICES = [('BUY', 'Buy/Long'), ('SELL', 'Sell/Short')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trades', null=True, blank=True)
    exchange_account = models.ForeignKey(ExchangeAccount, on_delete=models.SET_NULL, null=True, blank=True)
    symbol = models.CharField(max_length=20)
    side = models.CharField(max_length=10, choices=SIDE_CHOICES)
    entry_price = models.DecimalField(max_digits=20, decimal_places=8)
    exit_price = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
    quantity = models.DecimalField(max_digits=25, decimal_places=8)
    fees = models.DecimalField(max_digits=15, decimal_places=4, default=0.0000)
    pnl = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    notes = models.TextField(blank=True, null=True)
    opened_at = models.DateTimeField()
    closed_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.exit_price and self.quantity:
            if self.side == 'BUY':
                self.pnl = (self.exit_price - self.entry_price) * self.quantity - self.fees
            else:
                self.pnl = (self.entry_price - self.exit_price) * self.quantity - self.fees
        super().save(*args, **kwargs)