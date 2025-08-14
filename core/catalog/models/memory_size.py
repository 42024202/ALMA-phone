from __future__ import annotations
from django.db import models


class MemorySize(models.Model):
    size = models.PositiveIntegerField(
            verbose_name="Объем памяти"
            )

    def __str__(self) -> str:
        return f"{self.size} GB"

    class Meta:
        verbose_name = "Объем памяти"
        verbose_name_plural = "Объемы памяти"

