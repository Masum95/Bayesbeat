from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class FileSourceChoices(TextChoices):
    MOBILE = 'MOBILE', _('MOBILE')
    WATCH = 'WATCH', _('WATCH')



