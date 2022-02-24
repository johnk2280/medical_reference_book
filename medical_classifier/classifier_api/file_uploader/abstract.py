from abc import ABC
import csv
from datetime import datetime
from typing import Callable, Optional

import openpyxl

from classifier_api.models import Catalog
from classifier_api.models import CatalogItem


def _read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=';')
        for row in reader:
            yield row


def _read_xlsx(file_path):
    pass


class FileUploader(ABC):
    file_path: str
    model: Optional[Catalog, CatalogItem]

    method_mapper = {
        'csv': _read_csv,
        'xlsx': _read_xlsx,
    }

    def __init__(self, file_path, model):
        self.file_path = file_path
        self.model = model

    def read(self):
        extension = self.file_path.split('.')[-1]
        reader = self.method_mapper[extension](self.file_path)
        headers = next(reader)
        return map(lambda x: dict(zip(headers, x)), reader)

    def save(self):
        items = self.read()
        new_records = Catalog.objects.bulk_create(
            map(
                lambda x: self.model(**x),
                items,
            )
        )
        return True
