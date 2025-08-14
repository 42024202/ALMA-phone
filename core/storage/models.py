from __future__ import annotations
from django.db import models
from catalog.models.phone import Phone
from catalog.models.color import Color
from catalog.models.frame import Frame
from catalog.models.memory_size import MemorySize


class Stock(models.Model):
    """Phones in stock"""
    phone = models.ForeignKey(
            Phone,
            on_delete=models.CASCADE,
            related_name='stocks',
            verbose_name="Телефон"
            )

    color = models.ForeignKey(
            Color,
            on_delete=models.CASCADE,
            verbose_name="Цвет телефона"
            )

    memory_size = models.ForeignKey(
            MemorySize,
            on_delete=models.CASCADE,
            verbose_name="Объем памяти"
            )

    quantity = models.PositiveIntegerField(
            verbose_name="Количество"
            )

    frame = models.ForeignKey(
            Frame,
            on_delete=models.CASCADE,
            verbose_name="Корпус"
            )

    def __str__(self) -> str:
        return f"{self.phone} {self.color} {self.quantity} {self.memory_size} GB"

    class Meta:
        verbose_name = "Телефон в наличии"
        verbose_name_plural = "Телефоны в наличии"

