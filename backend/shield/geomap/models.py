from django.db import models
from core.models import BaseSecurityModel

class ThreatLocation(BaseSecurityModel):
    ip_address = models.GenericIPAddressField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    asn = models.CharField(max_length=50, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    is_vpnor_proxy = models.BooleanField(default=False)
    severity = models.CharField(max_length=50) # Low, Medium, High, Critical
    attack_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
