from django.db import models
from core.models import BaseSecurityModel

class SecurityPlaybook(BaseSecurityModel):
    name = models.CharField(max_length=255)
    trigger = models.CharField(max_length=255)
    actions = models.JSONField() # Sequence of steps
    is_automated = models.BooleanField(default=False)
    version = models.CharField(max_length=20, default='1.0')
    is_active = models.BooleanField(default=True)
    author = models.CharField(max_length=255, blank=True)

class AutomationExecution(BaseSecurityModel):
    playbook = models.ForeignKey(SecurityPlaybook, on_delete=models.CASCADE)
    target_resource = models.CharField(max_length=255)
    trigger_source = models.CharField(max_length=255, blank=True)
    affected_entities = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=50) # Running, Completed, Failed
    execution_log = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
