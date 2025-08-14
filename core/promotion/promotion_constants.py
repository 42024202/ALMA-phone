from django.db import models


class BannerTypeChoise(models.TextChoices):
    INDEX_HEAD = 'index_head', 'head banner on index page'
    INDEX_MIDDLE = 'index_middle', 'middle banner on index page'
    CATALOG_HEAD = 'catalog_head', 'head banner on catalog page'
    BRAND_HEAD = 'brand_head', 'head banner on brand page'

