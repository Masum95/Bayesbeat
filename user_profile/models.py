from django.db import models
import uuid

from Bayesbeat.settings import MEDIA_ROOT
from user_profile import enums
from user_profile.querysets import FileQuerySet
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


def get_uuid():
    return uuid.uuid4()


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


class WatchDistributionModel(models.Model):
    registration_id = models.CharField(max_length=36, default=get_uuid, editable=False, unique=True)

    user_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, help_text="Mobile no of user")

    watch_id = models.CharField(max_length=30)
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return '{} {} ({})'.format(self.user_name, self.watch_id, self.start_time)


class UserHealthProfile(models.Model):
    user = models.ForeignKey(WatchDistributionModel, on_delete=models.CASCADE)
    height = models.CharField(max_length=20, blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)

    dob = models.DateField(auto_now_add=False, blank=True, null=True)
    gender = models.CharField(
        max_length=5,
        choices=enums.GenderChoice.choices,
        blank=True,
        null=True
    )

    blood_group = models.CharField(
        max_length=5,
        choices=enums.BloodGroupChoices.choices,
        blank=True,
        null=True
    )



