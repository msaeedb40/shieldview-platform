from django.db import models
from core.models import BaseSecurityModel

class SecurityPolicy(BaseSecurityModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    policy_type = models.CharField(max_length=100) # e.g., Network, Identity, Data
    rules = models.JSONField(default=list)
    is_active = models.BooleanField(default=True)
    version = models.IntegerField(default=1)
    priority = models.IntegerField(default=100)
    enforcement_mode = models.CharField(max_length=50, default='monitoring') # blocking, monitoring, disabled
    owner = models.CharField(max_length=255, blank=True)
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.name} (v{self.version})"

# AI/ML Security Models
class AnomalyModel(BaseSecurityModel):
    name = models.CharField(max_length=255)
    algorithm = models.CharField(max_length=100)
    training_data_start = models.DateTimeField()
    training_data_end = models.DateTimeField()
    detection_threshold = models.FloatField(default=0.95)
    last_trained = models.DateTimeField(auto_now=True)

class AIPromptLog(BaseSecurityModel):
    user_id = models.CharField(max_length=255)
    prompt_text = models.TextField()
    response_text = models.TextField()
    is_injection_attempt = models.BooleanField(default=False)
    sensitivity_score = models.FloatField(default=0.0) # Score for data leakage

# Threat Intelligence (CTI) Models
class IntelligenceFeed(BaseSecurityModel):
    source_name = models.CharField(max_length=255)
    feed_url = models.URLField()
    api_key = models.CharField(max_length=512, blank=True)
    is_active = models.BooleanField(default=True)

class IndicatorOfCompromise(BaseSecurityModel):
    TYPE_CHOICES = (('IP', 'IP Address'), ('DOMAIN', 'Domain'), ('HASH', 'File Hash'), ('URL', 'URL'))
    ioc_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    value = models.CharField(max_length=512)
    confidence_score = models.FloatField(default=0.0)
    source_feed = models.ForeignKey(IntelligenceFeed, on_delete=models.CASCADE, null=True, blank=True)
    first_seen = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
