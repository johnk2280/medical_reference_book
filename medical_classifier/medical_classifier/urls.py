from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Classifier API',
        default_version='v1',
        description="""
        Documentation
        The `ReDoc` view can be found [here](/doc)
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='johnk2280@gmail.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('classifier_api.urls')),
    path(
        'swagger/<str:format>',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        '',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'doc',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-doc',
    ),

]
