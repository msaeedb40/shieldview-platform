from django.db import models
from core.models import BaseSecurityModel

class ComplianceStandard(BaseSecurityModel):
    name = models.CharField(max_length=255) # e.g., SOC2, HIPAA, GDPR
    description = models.TextField(blank=True)
    requirements = models.JSONField(default=list)
    version = models.CharField(max_length=50, default='1.0')
    is_active = models.BooleanField(default=True)

class MitigationPlan(BaseSecurityModel):
    standard = models.ForeignKey(ComplianceStandard, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    steps = models.JSONField(default=list)
    risk_level = models.CharField(max_length=50)
    mitigation_type = models.CharField(max_length=100, default='detective') # preventive, detective, corrective
    remediated_at = models.DateTimeField(null=True, blank=True)

class RemediationTask(BaseSecurityModel):
    plan = models.ForeignKey(MitigationPlan, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    status = models.CharField(max_length=50, default='pending') # pending, in-progress, completed
    assigned_to = models.CharField(max_length=255)
    priority = models.IntegerField(default=1)
    remediation_steps = models.JSONField(default=list, blank=True)

class SBOMRecord(BaseSecurityModel):
    app_name = models.CharField(max_length=255)
    version = models.CharField(max_length=100)
    dependency_list = models.JSONField() # Full list of packages and versions
    vulnerability_scan_id = models.CharField(max_length=255, blank=True)
    last_scan = models.DateTimeField(auto_now=True)
