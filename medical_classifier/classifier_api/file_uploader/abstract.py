import io
from abc import ABC
import csv
from datetime import datetime
from typing import Callable, Optional, Generator

import openpyxl
from django.core.files.uploadedfile import InMemoryUploadedFile

from classifier_api.models import Catalog
from classifier_api.models import CatalogItem


def _read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f_obj:
        reader = csv.DictReader(f_obj, delimiter=';')
        for obj in reader:
            yield obj


def _read_xlsx(file_path):
    pass


class FileUploader(ABC):
    model_name: str
    parent_id: Optional[str]

    methods_mapper = {
        'csv': _read_csv,
        'xlsx': _read_xlsx,
    }
    models_mapper = {
        'catalog': Catalog,
        'catalog_item': CatalogItem,
    }

    def __init__(self, file, model_name, parent_id=None):
        self.file = file
        self.model_name = model_name
        self.parent_id = parent_id

    def get_reader(self):
        if isinstance(self.file, InMemoryUploadedFile):
            self.file.open('r')
            reader = csv.DictReader(io.TextIOWrapper(self.file), delimiter=';')
            return reader

        extension = self.file.split('.')[-1]
        reader = self.methods_mapper[extension](self.file)
        return reader

    def save(self) -> bool:
        Catalog.objects.bulk_create(
            map(
                lambda x: self.models_mapper[self.model_name](
                    id=x['id'],
                    title=x['title'],
                    short_title=x['short_title'],
                    description=x['description'],
                    valid_from=datetime.strptime(x['valid_from'], '%d.%m.%Y')
                ),
                self.get_reader(),
            )
        )
        return True
