from django.db import models
from core.models import BaseSecurityModel

class IntegrationConfig(BaseSecurityModel):
    provider_name = models.CharField(max_length=255) # e.g., Splunk, Elastic, Slack
    api_key = models.CharField(max_length=512)
    endpoint_url = models.URLField(blank=True, null=True)
    config_params = models.JSONField(default=dict)
    is_connected = models.BooleanField(default=False)
    sync_status = models.CharField(max_length=50, default='idle') # idle, syncing, failed
    error_message = models.TextField(blank=True, null=True)
    last_sync = models.DateTimeField(null=True, blank=True)

class ThirdPartyRisk(BaseSecurityModel):
    vendor_name = models.CharField(max_length=255)
    risk_score = models.FloatField(default=0.0)
    assessment_date = models.DateField()
    compliant_status = models.BooleanField(default=False)
    findings = models.TextField(blank=True)
    mitigation_strategy = models.TextField(blank=True)
