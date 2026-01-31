from django.db import models
import uuid

class BaseSecurityModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    metadata = models.JSONField(default=dict, blank=True)
    tags = models.JSONField(default=list, blank=True)
    data_sensitivity = models.CharField(max_length=50, default='low') # low, medium, high, critical

    class Meta:
        abstract = True
