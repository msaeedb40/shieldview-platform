from django.db import models
from core.models import BaseSecurityModel

class SystemSetting(BaseSecurityModel):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    setting_group = models.CharField(max_length=100, default='general')
    is_readonly = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.key

class UserPreference(BaseSecurityModel):
    user_id = models.CharField(max_length=255, index=True)
    theme = models.CharField(max_length=50, default='dark')
    notifications_enabled = models.BooleanField(default=True)
    notification_settings = models.JSONField(default=dict, blank=True)
    dashboard_layout = models.JSONField(default=dict)

    class Meta:
        unique_together = ('user_id',)
