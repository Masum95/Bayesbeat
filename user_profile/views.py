import json
import os

import pdfkit
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.views.static import serve
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from Bayesbeat import settings
from .models import MyFile, WatchDistributionModel, UserHealthProfile
from .serializers import MyFileSerializer, UserHealthProfileSerializer
from user_profile import pagination, enums

from django.views.decorators.csrf import csrf_exempt

from .signal_analysis.pdf_generation import processed_sig_from_file, pdf_generate


class MedicalProfileView(ListCreateAPIView):
    serializer_class = UserHealthProfileSerializer
    pagination_class = pagination.CustomPagination

    def get_queryset(self):
        registration_id = self.request.query_params['registration_id']
        distroDetails = WatchDistributionModel.objects.get(registration_id=registration_id)
        return UserHealthProfile.objects.filter(user=distroDetails)

    def get(self, request, *args, **kwargs):
        return super(MedicalProfileView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.data)
        print(list(request.POST.items()))
        print("------0000000000")
        ser = UserHealthProfileSerializer(data=request.data)
        if ser.is_valid():
            print("ok ")
        else:
            print(ser.errors)  # To see the form errors in the console.

        return super(MedicalProfileView, self).post(request, *args, **kwargs)


def getMyFilteredFileList(query_params):
    queryset = MyFile.objects.all().order_by('-timestamp')
    start_time = query_params.get('start_time')
    end_time = query_params.get('end_time')
    if 'registration_id' in query_params:
        distroDetails = WatchDistributionModel.objects.get(registration_id=query_params.get('registration_id'))
        if not start_time:
            start_time = distroDetails.start_time
        else:
            start_time = max(distroDetails.start_time, start_time)

        if not end_time:
            end_time = distroDetails.end_time
        else:
            end_time = min(distroDetails.end_time, end_time)
        print(start_time, end_time)
        queryset = queryset.filter(device_id=distroDetails.watch_id)

        if start_time:
            queryset = queryset.get_after_time(start_time=start_time)
        if end_time:
            queryset = queryset.get_before_time(end_time=end_time)

    if 'device_id' in query_params:
        queryset = queryset.filter(device_id=query_params.get('device_id'))

    if 'selective' in query_params:
        queryset = queryset.filter(file_src=enums.FileSourceChoices.WATCH).filter(has_sent_to_mobile=False)
    return queryset


class MyFileView(ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = MyFileSerializer
    pagination_class = pagination.CustomPagination

    def get_queryset(self):
        return MyFile.objects.all().order_by('-timestamp')

    def filter_queryset(self, queryset):
        print(enums.FileSourceChoices.WATCH.name)
        query_params = self.request.query_params
        queryset = getMyFilteredFileList(query_params)
        print('here ', queryset)
        return queryset

    def post(self, request, *args, **kwargs):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_200_OK)
        else:
            print(file_serializer.errors)
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


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_watch_id(request):
    query_params = request.GET
    phone_num = query_params.get('phone_num')
    user_name = query_params.get('user_name')
    print(phone_num)
    distroDetails = None
    try:
        distroDetails = WatchDistributionModel.objects.get(phone=phone_num, user_name=user_name)
        print('---------', distroDetails)

        return JsonResponse({'status': "success", 'device_id': distroDetails.watch_id,
                             'registration_id': distroDetails.registration_id},
                            safe=False)  # or JsonResponse({'data': data})
    except ObjectDoesNotExist:
        print('nai ksu ')
        # return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'status': "failure"}, safe=False)  # or JsonResponse({'data': data})@api_view(('GET',))


def pdfGenerate(request):
    query_params = request.GET
    queryset = getMyFilteredFileList(query_params)
    regi_id = query_params.get('registration_id')
    user_name = UserHealthProfile.objects.get(user=regi_id).name
    output_file_name = user_name + "record" if user_name else regi_id + "record"
    print(MyFileSerializer(queryset, many=True).data[0])
    file_name = MyFileSerializer(queryset, many=True).data[0]['file']
    # file_ = open(file_name)

    (final_output, layer6_output, new_freq) = processed_sig_from_file(file_name)

    pdf_generate(output_file_name, final_output, ["Suspected AF"] * len(final_output), [1606507067] * len(final_output))
    test_file = open(os.path.join(settings.BASE_DIR, output_file_name+'.pdf'), 'rb')
    response = HttpResponse(content=test_file)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename="%s.pdf"' \
                                      % output_file_name + '.pdf'
    return response
