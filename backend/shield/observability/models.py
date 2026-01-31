from django.db import models
from core.models import BaseSecurityModel

class PerformanceMetric(BaseSecurityModel):
    metric_type = models.CharField(max_length=100) # CPU, Memory, Throughput
    value = models.FloatField()
    unit = models.CharField(max_length=20)
    resource_id = models.CharField(max_length=255, blank=True)
    tags = models.JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class SecurityLog(BaseSecurityModel):
    LEVELS = (('INFO', 'INFO'), ('WARN', 'WARN'), ('ERROR', 'ERROR'), ('CRITICAL', 'CRITICAL'))
    level = models.CharField(max_length=20, choices=LEVELS)
    service = models.CharField(max_length=100)
    message = models.TextField()
    trace_id = models.CharField(max_length=255, blank=True)
    source_ip = models.GenericIPAddressField(null=True, blank=True)
    context = models.JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class DeepQuery(BaseSecurityModel):
    name = models.CharField(max_length=255)
    query_string = models.TextField()
    category = models.CharField(max_length=100) # Threat Hunting, Audit, Compliance
    created_by = models.CharField(max_length=255)
    execution_count = models.IntegerField(default=0)
    last_run = models.DateTimeField(null=True, blank=True)

# Advanced Observability Models
class NetFlowAggregate(BaseSecurityModel):
    source_subnet = models.CharField(max_length=50)
    dest_subnet = models.CharField(max_length=50)
    protocol = models.CharField(max_length=20)
    total_bytes = models.BigIntegerField()
    flow_count = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class SystemProcessLog(BaseSecurityModel):
    host_id = models.CharField(max_length=255)
    process_name = models.CharField(max_length=255)
    pid = models.IntegerField()
    ppid = models.IntegerField() # Parent PID
    command_line = models.TextField()
    user = models.CharField(max_length=255)
    checksum = models.CharField(max_length=512, blank=True) # Binary hash
