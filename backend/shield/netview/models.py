from django.db import models
from core.models import BaseSecurityModel

class NetworkTopology(BaseSecurityModel):
    resource_id = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=100) # VPC, Subnet, Instance
    connections = models.JSONField(default=list) # List of connected resource IDs
    vlan_id = models.CharField(max_length=50, blank=True)
    subnet_mask = models.CharField(max_length=50, blank=True)
    tags = models.JSONField(default=dict)

class VPCLog(BaseSecurityModel):
    source_ip = models.GenericIPAddressField()
    dest_ip = models.GenericIPAddressField()
    source_port = models.IntegerField()
    dest_port = models.IntegerField()
    protocol = models.CharField(max_length=20)
    direction = models.CharField(max_length=20, default='inbound') # inbound, outbound
    action = models.CharField(max_length=20) # ALLOW, REJECT
    bytes_transferred = models.BigIntegerField()
