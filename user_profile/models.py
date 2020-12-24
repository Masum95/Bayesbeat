from django.db import models

from Bayesbeat.settings import MEDIA_ROOT
from user_profile import enums
from user_profile.querysets import FileQuerySet
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

class MyFile(models.Model):

    file = models.FileField(upload_to='', blank=False, null=False, unique=True, storage=gd_storage)
    file_name = models.CharField(max_length=75)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=False)
    device_id = models.CharField(max_length=50)
    has_sent_to_mobile = models.BooleanField(default=False)
    file_src =  models.CharField(
        max_length=6,
        choices=enums.FileSourceChoices.choices,
        default=enums.FileSourceChoices.WATCH,
        blank=False
    )
    objects = FileQuerySet.as_manager()

    def __str__(self):
        return '{} {} ({})'.format(self.device_id, self.timestamp, self.file)
