from django.db import models
from core.models import BaseSecurityModel

class WAFLog(BaseSecurityModel):
    client_ip = models.GenericIPAddressField()
    request_method = models.CharField(max_length=10)
    request_url = models.TextField()
    attack_type = models.CharField(max_length=100) # SQLi, XSS, etc.
    matched_rule_id = models.CharField(max_length=255)
    action = models.CharField(max_length=20) # Blocked, Logged
    payload_snippet = models.TextField(blank=True)
    user_agent = models.TextField(blank=True)
    country_code = models.CharField(max_length=5, blank=True)
    response_code = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class WAFRule(BaseSecurityModel):
    name = models.CharField(max_length=255)
    pattern = models.TextField() # Regex or similar
    category = models.CharField(max_length=100, default='custom') # OWASP, Custom, CVE
    is_enabled = models.BooleanField(default=True)
    severity = models.CharField(max_length=50)
    action_type = models.CharField(max_length=20, default='block') # block, allow, challenge
