from __future__ import annotations
from django.core.validators import MinValueValidator
from django.db import models 


class Display(models.Model):
    display_size = models.CharField(
            max_length=50,
            verbose_name='Размер экрана',
            )

    display_type = models.CharField(
            max_length=50,
            verbose_name='Тип экрана',
            )

    refresh_rate = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            validators=[MinValueValidator(1)],
            verbose_name='Частота обновления',
            )
    
    def __str__(self) -> str:
        return f"{self.display_size} {self.display_type} {self.refresh_rate} gHz"

    class Meta:
        verbose_name = 'Дисплей'
        verbose_name_plural = 'Дисплеи'

