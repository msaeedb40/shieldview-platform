from django.db import models
from core.models import BaseSecurityModel

class SecurityIncident(BaseSecurityModel):
    title = models.CharField(max_length=255)
    severity = models.CharField(max_length=50) # Low, Medium, High, Critical
    status = models.CharField(max_length=50) # Open, Investigating, Resolved, Closed
    source = models.CharField(max_length=255)
    timeline = models.JSONField(default=list)
    affected_resources = models.JSONField(default=list, blank=True)
    assigned_team = models.CharField(max_length=255, blank=True)

class IncidentMitigation(BaseSecurityModel):
    incident = models.ForeignKey(SecurityIncident, on_delete=models.CASCADE)
    action_taken = models.TextField()
    taken_by = models.CharField(max_length=255)
    mitigation_id = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class IncidentRemediation(BaseSecurityModel):
    incident = models.ForeignKey(SecurityIncident, on_delete=models.CASCADE)
    plan = models.TextField()
    resolution_steps = models.JSONField(default=list)
    is_verified = models.BooleanField(default=False)
    verification_method = models.CharField(max_length=255, blank=True)
    remediated_at = models.DateTimeField(null=True, blank=True)
