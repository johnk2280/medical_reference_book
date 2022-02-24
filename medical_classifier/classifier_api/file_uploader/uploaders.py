from .abstract import FileUploader
from ..models import Catalog


class CatalogFileUploader(FileUploader):

    def save(self):
        catalogs = self.read()
        new_records = Catalog.objects.bulk_create(
            map(
                lambda x: Catalog(**x),
                catalogs,
            )
        )
        return True


class CatalogItemFileUploader(FileUploader):

    def save(self):
        catalogs = self.read()
        new_records = Catalog.objects.bulk_create(
            map(
                lambda x: Catalog(**x),
                catalogs,
            )
        )
        return True