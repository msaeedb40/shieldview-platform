from django.db import models
from core.models import BaseSecurityModel

class AuditLog(BaseSecurityModel):
    actor = models.CharField(max_length=255) # User ID or Service Name
    action = models.CharField(max_length=255) # e.g., UPDATE_POLICY, DELETE_USER
    resource = models.CharField(max_length=255) # e.g., security.SecurityPolicy:uuid
    previous_state = models.JSONField(null=True)
    new_state = models.JSONField(null=True)
    impact_level = models.CharField(max_length=50, default='low') # low, medium, high, critical
    audit_type = models.CharField(max_length=50, default='automated') # manual, automated
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
