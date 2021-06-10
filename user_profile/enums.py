from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class FileSourceChoices(TextChoices):
    MOBILE = 'MOBILE', _('MOBILE')
    WATCH = 'WATCH', _('WATCH')


class BloodGroupChoices(TextChoices):
    ABP= 'AB+', 'AB+'
    ABN = 'AB-', 'AB-'
    AP = 'A+', 'A+'
    AN = 'A-', 'A-'
    BP = 'B+', 'B+'
    BN = 'B-', 'B-'
    OP = 'O+', 'O+'
    ON = 'O-', 'O-'


class GenderChoice(TextChoices):
    MALE = 'M', _('Male')
    FEMALE = 'F', _('Female')
    OTHER = 'O', _('Other')

