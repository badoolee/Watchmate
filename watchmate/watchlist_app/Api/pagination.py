from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)


class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "p"
    page_size_query_param = "size"
    max_page_size = 2
    last_page_strings = "end"


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 2
    limit_query_param = "limit"
    offset_query_param = "start"


class WatchListCPagination(CursorPagination):
    page_size = 2
    ordering = "created"
