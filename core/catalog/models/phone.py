from __future__ import annotations
from django.db import models
from catalog.models.battery import Battery
from catalog.models.display import Display
from catalog.models.brand import Brand
from catalog.models.country import CountryOfOrigin
import datetime
from catalog.constants import (
        MIN_PRICE, MIN_CPU_CORES, MIN_CPU_FREQUENCY, MIN_RAM
        )
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from catalog.constants import PhoneVersionChoise


class Phone(models.Model):
    brand = models.ForeignKey(
            Brand,
            on_delete=models.CASCADE,
            verbose_name="Бренд"
            )

    model = models.CharField(
            max_length=50,
            verbose_name="Модель телефона"
            )

    phone_version = models.CharField(
            choices=PhoneVersionChoise,
            verbose_name="Версия телефона"
            )

    price = models.DecimalField(
            max_digits=10,
            decimal_places=2,
            validators=[MinValueValidator(MIN_PRICE)],
            verbose_name="Цена телефона"
            )
    
    description = models.TextField(
            verbose_name="Описание телефона"
            )

    battery = models.ForeignKey(
            Battery,
            on_delete=models.CASCADE,
            verbose_name="Батарея"
            )

    display = models.ForeignKey(
            Display,
            on_delete=models.CASCADE,
            verbose_name="Дисплей"
            )

    oc_version = models.CharField(
            max_length=50,
            verbose_name="Версия ОС"
            )
    
    cover_photo = models.ImageField(
            upload_to="cover_photos/",
            verbose_name="Главная фотография"
            )

    phone_cpu = models.CharField(
            max_length=50,
            verbose_name="Процессор телефона"
            )
    
    cpu_cores = models.PositiveSmallIntegerField(
            validators=[MinValueValidator(MIN_CPU_CORES)],
            verbose_name="Количество ядер процессора"
            )

    cpu_frequency = models.DecimalField(
            max_digits=4,
            decimal_places=2,
            validators=[MinValueValidator(MIN_CPU_FREQUENCY)],
            verbose_name="Частота процессора"
            )

    ram = models.PositiveSmallIntegerField(
            verbose_name='ОЗУ',
            validators=[MinValueValidator(MIN_RAM)],
            )
    
    network = models.CharField(
            max_length=50,
            verbose_name="Сеть"
            )

    wifi_standart = models.CharField(
            max_length=50,
            verbose_name="Стандарт WiFi"
            )

    bluetooth_standart = models.CharField(
            max_length=50,
            verbose_name="Стандарт Bluetooth"
            )

    nfs_support = models.BooleanField(
            default=True,
            verbose_name="Поддержка NFS"
            )
    
    release_year = models.PositiveSmallIntegerField(
            verbose_name="Год выпуска"
            )

    country_of_origin = models.ForeignKey(
            CountryOfOrigin,
            on_delete=models.CASCADE,
            verbose_name="Страна производства"
            )
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.phone_version}"

    def clean_year(self) -> None:
        """Check if release year is not older than current year"""
        current_year = datetime.date.today().year
        if self.release_year > current_year:
            raise ValidationError({
                "release_year": f"Год выпуска не может быть больше {current_year}."
            })

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"


class PhoneImage(models.Model):
    phone = models.ForeignKey(
            Phone,
            on_delete=models.CASCADE,
            verbose_name="Фотографии телефона"
            )

    image = models.ImageField(
            upload_to="phone_images/",
            verbose_name="Фотографии телефона"
            )

    def __str__(self) -> str:
        return f"{self.phone} - {self.image.name}"

    class Meta:
        verbose_name = "Фотографии телефона"
        verbose_name_plural = "Фотографии телефонов"

