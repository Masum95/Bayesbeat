from django.db.models import Q, QuerySet
from django.contrib.auth import get_user_model


import datetime

from django.utils.datetime_safe import strftime


class FileQuerySet(QuerySet):
    def get_order_between_dates(self, start_time, end_time):
        return self.filter(
            timestamp__range=[start_time, end_time]
        )

    def get_after_time(self, start_time):
        # dt = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")

        return self.filter(
            timestamp__gte = start_time
        )

    def get_before_time(self, end_time):
        # dt = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")

        return self.filter(
            timestamp__lte = end_time
        )



