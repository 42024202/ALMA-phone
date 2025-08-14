from typing import TypeAlias
from django.db.models import QuerySet, Prefetch
from catalog.models.phone import Phone
from storage.models import Stock

PhonesQuery: TypeAlias = QuerySet[Phone]

def get_all_phones() -> PhonesQuery:
    """Returns all phones with their variants"""
    return Phone.objects.prefetch_related(
        Prefetch(
            "stocks",
            queryset=Stock.objects.select_related("color", "memory_size", "frame")
        )
    )

def get_phone_by_id(phone_id: int) -> PhonesQuery:
    """Returns phone with its variants"""
    return get_all_phones().filter(id=phone_id)

