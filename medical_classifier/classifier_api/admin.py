from django.contrib import admin

from .models import Catalog
from .models import CatalogItem

admin.site.register(Catalog)
admin.site.register(CatalogItem)
