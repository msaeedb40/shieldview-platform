from django.db import models
from core.models import BaseSecurityModel

class AnalyticsReport(BaseSecurityModel):
    title = models.CharField(max_length=255)
    report_type = models.CharField(max_length=100) # Monthly, Weekly, Custom
    data_payload = models.JSONField()
    parameters = models.JSONField(default=dict, blank=True)
    owner = models.CharField(max_length=255, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

class SecurityKPI(BaseSecurityModel):
    name = models.CharField(max_length=255) # e.g., Mean Time to Respond (MTTR)
    value = models.FloatField()
    target_value = models.FloatField(null=True)
    threshold = models.FloatField(null=True)
    is_breached = models.BooleanField(default=False)
    trend = models.CharField(max_length=20) # Up, Down, Stable
