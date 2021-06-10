from rest_framework import serializers

from Bayesbeat.settings import MEDIA_ROOT
from .models import MyFile, WatchDistributionModel, UserHealthProfile

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
        device_id = validated_data['device_id']
        try:
            obj = MyFile.objects.get(device_id=validated_data['device_id'], file_name=validated_data['file'].name)
            print('exists')
        except:
            try:
                distroDetails = WatchDistributionModel.objects.get(watch_id=device_id)
                if (not distroDetails.end_time) or (distroDetails.end_time and datetime.now() <= distroDetails.end_time ):
                    obj = MyFile.objects.create(**validated_data)

            except:
                pass
            print('new')

        return obj


class UserHealthProfileSerializer(serializers.ModelSerializer):
    registration_id = serializers.CharField(write_only=True)


    class Meta:
        model = UserHealthProfile
        fields = '__all__'
        extra_kwargs = {"user": {"required": False}}

    def create(self, validated_data):
        """
          set request's user as feedback's author
        """
        print(validated_data, '------')
        print(self.errors)
        registration_id = validated_data.pop('registration_id')
        distroDetails = WatchDistributionModel.objects.get(registration_id=registration_id)

        healthProfile = UserHealthProfile.objects.create(user=distroDetails,
                                           **validated_data)
        return healthProfile

