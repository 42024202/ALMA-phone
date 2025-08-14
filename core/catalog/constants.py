from decimal import Decimal
from django.db import models

MIN_PRICE = Decimal("1")
MIN_CPU_CORES = 1
MIN_CPU_FREQUENCY = Decimal("1")  # ГГц
MIN_RAM = 1  # ГБ
MIN_VALUE = 1


class PhoneVersionChoise(models.TextChoices):
    """Phone version choices"""
    SLIM = 'SL', 'Slim'
    PRO = 'PR', 'Pro'
    STANDARD = 'ST', 'Standard'
    ULTRA = 'UL', 'Ultra'
    PRO_MAX = 'PM', 'Pro Max'
    PLUS = 'Pl', 'Plus'

