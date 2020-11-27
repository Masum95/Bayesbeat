from django.db import models


class MyFile(models.Model):
    file = models.FileField(blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=False)
    device_id = models.CharField(max_length=50)

    def __str__(self):
        return '{} {} ({})'.format(self.device_id, self.timestamp, self.file)
