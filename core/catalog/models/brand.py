from __future__ import annotations
from django.db import models 


class Brand(models.Model):
    name = models.CharField(
            max_length=50,
            verbose_name="Название бренда"
            )

    logo = models.ImageField(
            upload_to="brand_logos/",
            verbose_name="Логотип"
            )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

