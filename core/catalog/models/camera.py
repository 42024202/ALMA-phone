from __future__ import annotations
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models 
from catalog.models.phone import Phone


class Camera(models.Model):
    phone = models.ForeignKey(
            Phone,
            on_delete=models.CASCADE,
            verbose_name="Телефон"
            )

    type = models.CharField(
            max_length=50,
            verbose_name="Тип камеры"
            )

    resolution = models.CharField(
            max_length=50,
            verbose_name="Разрешение камеры"
            )

    features = models.CharField(
            max_length=100,
            verbose_name="Особенности камеры"
            )

    def __str__(self) -> str:
        return f"{self.type} {self.resolution}"

    class Meta:
        verbose_name = "Камера"
        verbose_name_plural = "Камеры"


class CameraModule(models.Model):
    camera = models.ForeignKey(
            Camera,
            on_delete=models.CASCADE,
            related_name="modules",
            verbose_name="Камера"
            )

    module_number = models.PositiveSmallIntegerField(
            validators=[MinValueValidator(1)],
            verbose_name="Номер модуля"
            )

    resolution = models.CharField(
            max_length=50,
            verbose_name="Разрешение модуля"
            )

    features = models.CharField(
            max_length=100,
            verbose_name="Особенности модуля"
            )

    def __str__(self) -> str:
        return f"{self.camera} {self.module_number} {self.resolution}"

    class Meta:
        verbose_name = "Модуль камеры"
        verbose_name_plural = "Модули камер"

