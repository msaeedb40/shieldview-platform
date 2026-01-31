from django.db import models
from core.models import BaseSecurityModel

class XDRDetectionLog(BaseSecurityModel):
    SOURCES = (
        ('endpoint', 'Endpoint'),
        ('cloud', 'Cloud'),
        ('network', 'Network'),
        ('email', 'Email'),
        ('identity', 'Identity'),
    )
    source_type = models.CharField(max_length=50, choices=SOURCES)
    severity = models.CharField(max_length=50)
    description = models.TextField()
    threat_category = models.CharField(max_length=100, blank=True)
    mitre_technique = models.CharField(max_length=100, blank=True)
    confidence_score = models.FloatField(default=0.0)
    raw_data = models.JSONField()
    correlation_id = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
