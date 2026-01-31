from django.db import models
from core.models import BaseSecurityModel

class NotificationRule(BaseSecurityModel):
    name = models.CharField(max_length=255)
    trigger_condition = models.JSONField() # e.g., severity >= High
    channel = models.CharField(max_length=50) # Email, Slack, Webhook
    recipient = models.CharField(max_length=255)
    template_id = models.CharField(max_length=100, blank=True)
    retry_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

class SecurityAlert(BaseSecurityModel):
    title = models.CharField(max_length=255)
    message = models.TextField()
    severity = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    source_incident_id = models.CharField(max_length=255, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
