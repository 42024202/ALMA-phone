from __future__ import annotations
from django.db import models


class CountryOfOrigin(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Страна производства'
        verbose_name_plural = 'Страны производства'

