# import json
# from rest_framework import status, response
#
#
# HTTP_400_BAD_REQUEST_SWAGGER_RESPONSE = json.dumps({
#     'detail': [
#         {'field_1': 'Error details'}
#     ]
# })
#
#
# HTTP_401_UNAUTHORIZED_SWAGGER_RESPONSE = json.dumps({
#     'detail': 'Authentication credentials were not provided'
# })
#
#
# HTTP_403_FORBIDDEN_SWAGGER_RESPONSE = json.dumps({
#     "detail": "You do not have permission to perform this action."
# })
#
#
# HTTP_404_RESPONSE_DICT = {'details': 'Not found'}
# HTTP_404_NOT_FOUND_SWAGGER_RESPONSE = json.dumps(HTTP_404_RESPONSE_DICT)
# HTTP_404_NOT_FOUND_RESPONSE = response.Response(
#     data=HTTP_404_RESPONSE_DICT,
#     status=status.HTTP_404_NOT_FOUND
# )
#
#
# def get_http_201_created_response(serializer):
#     return response.Response(
#         data=serializer.data,
#         status=status.HTTP_201_CREATED
#     )
#
#
# def get_http_400_bad_request_response(serializer):
#     return response.Response(
#         data=serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST
#     )
#
#
# def check_retrieve_update_destroy_permission(instance, request, obj):
#     """
#     :param instance: RetrieveUpdateDestroyAPIView instance
#     :param request: rest_framework.request.Request
#     :param obj: model object instance
#     :return: obj if it has the permission, calls APIView.permission_denied method otherwise
#     """
#     permission_method = obj.has_view_permission if request.method == 'GET' else obj.is_owner
#     if not permission_method(user=request.user):
#         instance.permission_denied(request)
#
#     return obj
#
#
