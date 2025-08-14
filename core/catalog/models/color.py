from __future__ import annotations
from django.db import models


class Color(models.Model):
    name = models.CharField(
            max_length=50,
            verbose_name="Цвет"
            )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

