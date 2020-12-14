from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import MyFile
from .serializers import MyFileSerializer
from user_profile import pagination


class MyFileView(ListCreateAPIView):

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = MyFileSerializer
    pagination_class = pagination.CustomPagination

    def get_queryset(self):
        return MyFile.objects.all().order_by('-timestamp')

    def filter_queryset(self, queryset):
        query_params = self.request.query_params
        if 'start_time' in query_params:
            queryset = queryset.get_after_time(start_time=query_params.get('start_time'))
        if 'end_time' in query_params:
            queryset = queryset.get_before_time(end_time=query_params.get('end_time'))
        if 'device_id' in query_params:
            queryset = queryset.filter(device_id=query_params.get('device_id'))
        return queryset

    def post(self, request, *args, **kwargs):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
