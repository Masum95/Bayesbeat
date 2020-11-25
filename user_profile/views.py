# todo: check for permission and filter the queryset accordingly
#
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

# from coreapp import permissions, models, pagination
# from coreapp.serializers.profile import ProfileSerializer, ProfileListSerializer
from user_profile import utils
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("eize ekhane ashsos")

#
#
# class ProfileListAPIView(generics.ListAPIView):
#     permission_classes = (permissions.IsAcceptedUser, )
#     # serializer_class = ProfileSerializer
#     pagination_class = pagination.CustomPagination
#     queryset = models.ProfileModel.objects.accepted_users()
#
#     def filter_queryset(self, queryset):
#         query_params = self.request.query_params
#         if 'search' in query_params:
#             queryset = queryset.search(search_text=query_params.get('search'))
#         if 'address' in query_params:
#             queryset = queryset.address(address_uuid=query_params.get('address'))
#         if 'country' in query_params:
#             queryset = queryset.country(country=query_params.get('country'))
#         if 'workplace' in query_params:
#             queryset = queryset.workplace(workplace_uuid=query_params.get('workplace'))
#         if 'department' in query_params or 'batch' in query_params:
#             queryset = queryset.filter_by_batch_department(
#                 batch=query_params.get('batch'),
#                 department=query_params.get('department')
#             )
#
#         return queryset
#
#     def get(self, request, *args, **kwargs):
#         return super(ProfileListAPIView, self).get(request, *args, **kwargs)
#
#
# class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
#     permission_classes = (permissions.HasProfileRetrieveUpdatePermission, )
#     serializer_class = ProfileSerializer
#     lookup_field = 'uuid'
#     queryset = models.ProfileModel.objects.accepted_users()
#
#     def get(self, request, *args, **kwargs):
#         return super(ProfileRetrieveUpdateView, self).get(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         # todo: should I block this ENDPOINT?
#         return super(ProfileRetrieveUpdateView, self).put(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super(ProfileRetrieveUpdateView, self).patch(request, *args, **kwargs)
#
#
# class MyProfileView(generics.RetrieveAPIView):
#     permission_classes = (IsAuthenticated, )
#     serializer_class = ProfileSerializer
#
#     def get_object(self):
#         return self.request.user.profile
#
#
#     def get(self, request, *args, **kwargs):
#         return super(MyProfileView, self).get(request, *args, **kwargs)
#
