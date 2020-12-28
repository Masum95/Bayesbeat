from rest_framework import serializers

from Bayesbeat.settings import MEDIA_ROOT
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
        print(data, data['file'].name)
        datetime_obj_with_tz = make_aware(datetime.fromtimestamp(int(data['timestamp'])))
        data['timestamp'] = datetime_obj_with_tz
        data['file_name'] = data['file'].name
        return super(MyFileSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        print('here in create ', validated_data['file'].name)
        obj = None
        try:
            obj = MyFile.objects.get(device_id=validated_data['device_id'], file_name=validated_data['file'].name)
            print('exists')
        except:
            obj = MyFile.objects.create(**validated_data)
            print('new')
        # print(MyFile.objects.filter(device_id=validated_data['device_id'], file_name=validated_data['file'].name))
        # person, created = MyFile.objects.get_or_create( **validated_data)
        #
        # print(person, created)
        # if created:
        #     print('new ')
        # else:
        #     print('exists')
        return obj



