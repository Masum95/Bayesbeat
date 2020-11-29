from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import MyFile
from .serializers import MyFileSerializer


class MyFileView(ListCreateAPIView):

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = MyFileSerializer

    def get_queryset(self):
        return MyFile.objects.all()

    def post(self, request, *args, **kwargs):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
