from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc, context):
    """
    Extends django rest frameworks exception handling ability
    Must be set in settings:
    REST_FRAMEWORK = {
         # ...
         'EXCEPTION_HANDLER': 'buetian.exception_handler.exception_handler',
         # ...
    }
    """

    # Handle Django ValidationError as DRF serializers.ValidationError
    if isinstance(exc, DjangoValidationError):
        exc = DRFValidationError(detail=exc.message_dict)

    return drf_exception_handler(exc, context)
