from rest_framework import serializers
from .models import MyFile

from datetime import datetime

from django.utils.timezone import make_aware

class MyFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyFile
        fields = '__all__'

    def to_internal_value(self, data):
        """
        called before serializer validation.
        converts institute's uuid to id
        """

        datetime_obj_with_tz = make_aware(datetime.fromtimestamp(int(data['timestamp'])))
        data['timestamp'] = datetime_obj_with_tz
        return super(MyFileSerializer, self).to_internal_value(data)



