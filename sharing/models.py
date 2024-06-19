from djongo import models
from django.conf import settings

class SharedTracker(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE)
    shared_with = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shared_with', on_delete=models.CASCADE)
    can_edit = models.BooleanField(default=False)