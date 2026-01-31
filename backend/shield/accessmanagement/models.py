from django.db import models
from core.models import BaseSecurityModel

class UserProfile(BaseSecurityModel):
    ROLES = (
        ('admin', 'Administrator'),
        ('analyst', 'Security Analyst'),
        ('viewer', 'Viewer'),
    )
    external_id = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=50, choices=ROLES, default='viewer')
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    mfa_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.external_id} ({self.role})"

class AccessLog(BaseSecurityModel):
    ACTIONS = (
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('mfa_verify', 'MFA Verification'),
        ('elevate', 'Privilege Elevation'),
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='access_logs')
    action = models.CharField(max_length=50, choices=ACTIONS)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    is_success = models.BooleanField(default=True)
    failure_reason = models.TextField(blank=True, null=True)

# PAM Models
class PrivilegedAccount(BaseSecurityModel):
    account_name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=100) # Server, DB, Admin Panel
    credential_type = models.CharField(max_length=50, default='password')
    rotation_interval_days = models.IntegerField(default=90)
    last_rotated = models.DateTimeField(null=True, blank=True)

class AccessRequest(BaseSecurityModel):
    STATUS_CHOICES = (('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('DENIED', 'Denied'), ('EXPIRED', 'Expired'))
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    account = models.ForeignKey(PrivilegedAccount, on_delete=models.CASCADE)
    reason = models.TextField()
    duration_minutes = models.IntegerField(default=60)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    approver = models.CharField(max_length=255, null=True, blank=True)

class SessionRecording(BaseSecurityModel):
    access_request = models.OneToOneField(AccessRequest, on_delete=models.CASCADE)
    recording_url = models.URLField()
    events_log = models.JSONField(default=list)
    duration_seconds = models.IntegerField()
