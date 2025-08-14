from __future__ import annotations
from django.core.validators import MinValueValidator
from django.db import models


class Frame(models.Model):
    frame_material = models.CharField(
            max_length=255,
            verbose_name="Материал корпуса"
            )
    length = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            validators=[MinValueValidator(1)],
            verbose_name="Длина"
            )
    width = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            validators=[MinValueValidator(1)],
            verbose_name="Ширина"
            )
    height = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            validators=[MinValueValidator(1)],
            verbose_name="Высота"
            )
    weight = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            validators=[MinValueValidator(1)],
            verbose_name="Вес"
            )

    def __str__(self) -> str:
        return f"{self.frame_material} {self.length} {self.weight}"

    class Meta:
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуса"

