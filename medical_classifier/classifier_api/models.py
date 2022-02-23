from django.db import models


class Catalog(models.Model):
    id = models.CharField(
        verbose_name='идентификатор',
        primary_key=True,
        max_length=256,
     )
    title = models.CharField(
        verbose_name='наименование',
        max_length=128,
        unique=True,
        null=False,
    )
    short_title = models.CharField(
        verbose_name='краткое наименование',
        max_length=64,
        default='',
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        max_length=256,
        default='',
        blank=True,
    )
    version = models.CharField(
        verbose_name='версия',
        max_length=10,
        null=False,
    )
    valid_from = models.DateTimeField(
        verbose_name='действует с',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'catalog'
        verbose_name_plural = 'catalogs'


class CatalogItem(models.Model):
    id = models.CharField(
        verbose_name='идентификатор',
        primary_key=True,
        max_length=256,
    )
    catalog_id = models.ForeignKey(
        Catalog,
        verbose_name='идентификатор родительского справочника',
        on_delete=models.CASCADE,
    )
    code = models.CharField(
        verbose_name='код',
        max_length=128,
        unique=True,
        db_index=True,
        null=False,
    )
    value = models.CharField(
        verbose_name='значение',
        null=False,
        max_length=126,
    )

    def __str__(self):
        return f'{self.code} - {self.value}'

    class Meta:
        verbose_name = 'catalog item'
        verbose_name_plural = 'catalog items'
