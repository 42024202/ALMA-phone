from __future__ import annotations
from django.db import models
from promotion.promotion_constants import BannerTypeChoise


class Banner(models.Model):
    title = models.CharField(
            max_length=100,
            verbose_name="Название баннера"
            )

    is_active = models.BooleanField(
            default=True,
            verbose_name="Активен"
            )

    type_of_bunner = models.CharField(
            choices=BannerTypeChoise,
            verbose_name="Тип баннера"
            )

    description = models.TextField(
            verbose_name="Описание баннера"
            )

    cover_image = models.ImageField(
            upload_to='promotion/',
            verbose_name="Обложка баннера"
            )

    def __str__(self) -> str:
        return f"{self.title} {self.type_of_bunner}"

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class BannerImage(models.Model):
    banner = models.ForeignKey(
            Banner,
            on_delete=models.CASCADE,
            related_name='images',
            verbose_name="Баннер"
            )

    image = models.ImageField(
            upload_to='banner_images/',
            verbose_name="Изображения баннера"
            )
    
    class Meta:
        verbose_name = "Изображение баннера"
        verbose_name_plural = "Изображения баннера"

