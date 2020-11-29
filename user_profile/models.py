from django.db import models

from Bayesbeat.settings import MEDIA_ROOT
from user_profile.querysets import FileQuerySet


class MyFile(models.Model):
    file = models.FileField(upload_to=MEDIA_ROOT, blank=False, null=False, unique=True)
    file_name = models.CharField(max_length=75)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=False)
    device_id = models.CharField(max_length=50)
    objects = FileQuerySet.as_manager()

    def __str__(self):
        return '{} {} ({})'.format(self.device_id, self.timestamp, self.file)
