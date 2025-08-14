from __future__ import annotations
from django.db import models
from django.core.validators import MinValueValidator


class Battery(models.Model):
    capacity = models.PositiveSmallIntegerField(
            validators=[MinValueValidator(1)],
            verbose_name="Объем батареи"
            )

    type = models.CharField(
            max_length=50,
            verbose_name="Тип батареи"
            )
    
    fast_charging = models.BooleanField(
            default=True,
            verbose_name="Быстрая зарядка"
            )

    wireless_charging = models.BooleanField(
            default=False,
            verbose_name="Беспроводная зарядка"
            )

    removable = models.BooleanField(
            default=False,
            verbose_name="Возможность снятия"
            )

    def __str__(self) -> str:
        return f"{self.capacity} мАч"

    class Meta:
        verbose_name = "Батарея"
        verbose_name_plural = "Батареи"

