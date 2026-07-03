from django.db import models
from django.conf import settings

class Exchange(models.Model):
    name = models.CharField(max_length=50, unique=True)
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class ExchangeAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exchange_accounts')
    exchange = models.ForeignKey(Exchange, on_delete=models.PROTECT)
    account_name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=255)
    api_secret = models.TextField()
    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'account_name')

    def __str__(self):
        return f"{self.user.email} - {self.exchange.name} ({self.account_name})"