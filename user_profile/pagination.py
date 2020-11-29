from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    """
    Custom pagination class for paginating objects in response
    For documentation, see: https://www.django-rest-framework.org/api-guide/pagination/#configuration
    """

    django_paginator_class = Paginator
    page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000
    template = None

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', 1)),
            'page_size': min(
                int(self.request.GET.get('page_size', self.page_size)),
                self.max_page_size
            ),
            'data': data
        })