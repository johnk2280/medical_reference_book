from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import CatalogItemViewSet
from .views import CatalogItemFileUploadView
from .views import CatalogViewSet
from .views import CatalogFileUploadView


app_name = 'classifier_api'


router = DefaultRouter(trailing_slash=True)
router.register(r'catalogs', CatalogViewSet, basename='catalogs')
router.register(r'catalog_items', CatalogItemViewSet, basename='catalog_items')


urlpatterns = [
    path('', include(router.urls)),
    path('catalogs_upload/', CatalogFileUploadView.as_view()),
    path('catalog_items_upload/', CatalogItemFileUploadView.as_view()),
]
