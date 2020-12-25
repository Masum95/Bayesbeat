import json

from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import MyFile
from .serializers import MyFileSerializer
from user_profile import pagination, enums

from django.views.decorators.csrf import csrf_exempt


class MyFileView(ListCreateAPIView):

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = MyFileSerializer
    pagination_class = pagination.CustomPagination

    def get_queryset(self):
        return MyFile.objects.all().order_by('-timestamp')

    def filter_queryset(self, queryset):
        print(enums.FileSourceChoices.WATCH.name)
        query_params = self.request.query_params
        if 'start_time' in query_params:
            queryset = queryset.get_after_time(start_time=query_params.get('start_time'))
        if 'end_time' in query_params:
            queryset = queryset.get_before_time(end_time=query_params.get('end_time'))
        if 'device_id' in query_params:
            queryset = queryset.filter(device_id=query_params.get('device_id'))
        if 'selective' in query_params:
            queryset = queryset.filter(file_src=enums.FileSourceChoices.WATCH).filter(has_sent_to_mobile=False)
        print('here ' , queryset)
        return queryset

    def post(self, request, *args, **kwargs):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def file_ack_view(request):

    query_params = request.POST
    print('before ', request.body)
    body_unicode = request.body.decode('utf-8')
    print('here ', body_unicode)
    body = json.loads(body_unicode)
    content = body['file_list']
    if len(content) == 0:
        return JsonResponse({'message': 'Success'})

    file_list = content.split(',')[:-1]
    files = MyFile.objects.filter(file_name__in=file_list)
    print(files)
    files.update(has_sent_to_mobile=True)
    for object in files:
        object.save()

    return JsonResponse({'message': 'Success'})