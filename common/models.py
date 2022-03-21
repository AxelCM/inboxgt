#Django
from django.db import models

#Django Crum
from crum import get_current_user
from django.conf import settings

#DateTimeNative
from datetime import datetime

#Models
class DataControl(models.Model):
    """Use for update who modify some record"""
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True, related_name='%(app_label)s_%(class)s_creation')
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_updated' )
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract =  True
