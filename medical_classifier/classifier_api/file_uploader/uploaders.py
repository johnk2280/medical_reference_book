from .abstract import FileUploader
from ..models import Catalog


class CatalogFileUploader(FileUploader):
    pass


class CatalogItemFileUploader(FileUploader):
    def save(self) -> bool:
        Catalog.objects.bulk_create(
            map(
                lambda x: self.models_mapper[self.model_name](**x),
                self.get_reader(),
            )
        )
        try:
            self.file.close()
        except AttributeError:
            pass

        return True
