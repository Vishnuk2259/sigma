from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'pagination': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'total_pages': self.page.paginator.num_pages,
                'total_items': self.page.paginator.count
            },
            'results': data
        })

    def get_page_size(self, request):
        if self.page_size_query_param in request.GET:
            return int(request.GET[self.page_size_query_param])
        return self.page_size