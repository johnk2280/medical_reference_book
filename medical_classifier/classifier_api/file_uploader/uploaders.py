from .abstract import FileUploader
from ..models import Catalog


class CatalogFileUploader(FileUploader):
    pass


class CatalogItemFileUploader(FileUploader):
    pass

    # def save(self):
    #     catalogs = self.read()
    #     new_records = Catalog.objects.bulk_create(
    #         map(
    #             lambda x: Catalog(**x),
    #             catalogs,
    #         )
    #     )
    #     return True
