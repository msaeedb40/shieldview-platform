from django.db import models
from core.models import BaseSecurityModel

class ZeroTrustRule(BaseSecurityModel):
    name = models.CharField(max_length=255)
    identity_required = models.BooleanField(default=True)
    device_health_check_required = models.BooleanField(default=True)
    mfa_required = models.BooleanField(default=True)
    device_posture_required = models.BooleanField(default=True)
    allowed_roles = models.JSONField(default=list)

class DeviceHealthCheck(BaseSecurityModel):
    device_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    os_version = models.CharField(max_length=100)
    patch_level = models.CharField(max_length=100, blank=True)
    is_managed = models.BooleanField(default=True)
    is_encrypted = models.BooleanField(default=False)
    has_firewall = models.BooleanField(default=False)
    last_check = models.DateTimeField(auto_now=True)
    is_compliant = models.BooleanField(default=False)
