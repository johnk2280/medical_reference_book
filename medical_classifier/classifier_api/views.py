from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
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
    queryset = Catalog.objects.all()
