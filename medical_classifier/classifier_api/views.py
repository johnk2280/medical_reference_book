from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser

from .models import Catalog
from .models import CatalogItem
from .serializers import CatalogSerializer
from .serializers import CatalogItemSerializer


class CatalogViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    List of classifiers.
    """

    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()


class CatalogItemViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    List of classifier items.
    """

    serializer_class = CatalogItemSerializer
    queryset = CatalogItem.objects.all()


class CatalogUploadView(APIView):
    """
    Загрузка списка справочников из файла.
    """

    def post(self, request) -> Response:
        pass


class CatalogItemUploadView(APIView):
    """
    Загрузка списка элементов справочника из файла.
    Идентификатор родительского справочника и его версия должны быть указаны в
    имени загружаемого файла через нижнее подчеркивание:
    1.2.643.5.1.13.13.99.2.923_3.4_XLS
    """

    def post(self, request) -> Response:
        pass
