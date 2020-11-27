from django.db import models


class MyFile(models.Model):
    file = models.FileField(blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    device_id = models.CharField(max_length=50)

    def __str__(self):
        return '{} {} ({})'.format(self.device_id, self.recorded_at, self.file)
