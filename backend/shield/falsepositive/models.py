from django.db import models
from core.models import BaseSecurityModel

class FalsePositiveEvidence(BaseSecurityModel):
    incident_id = models.CharField(max_length=255) # Reference to security incident
    source = models.CharField(max_length=100) # WAF, XDR, etc.
    evidence_data = models.JSONField()
    reason_for_classification = models.TextField()
    reporter = models.CharField(max_length=255)

class SuppressionRule(BaseSecurityModel):
    name = models.CharField(max_length=255)
    condition_pattern = models.JSONField() # e.g., {"ip": "1.1.1.1", "pattern": "test"}
    is_active = models.BooleanField(default=True)
    expiry_date = models.DateTimeField(null=True, blank=True)

class FalsePositivePolicy(BaseSecurityModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    mitigation_strategy = models.TextField()
    remediation_steps = models.JSONField(default=list)
    enforcement_level = models.CharField(max_length=50, default='log_only') # log_only, blocking

class FPReviewWorkflow(BaseSecurityModel):
    evidence = models.ForeignKey(FalsePositiveEvidence, on_delete=models.CASCADE)
    suppression_rule = models.ForeignKey(SuppressionRule, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, default='pending_review')
    reviewer = models.CharField(max_length=255, null=True, blank=True)
    comments = models.TextField(blank=True)
