from __future__ import annotations
from catalog.models.color import Color
from catalog.models.memory_size import MemorySize
from catalog.models.brand import Brand
from catalog.models.phone import Phone


def get_all_colors() -> list[str]:
    return list(Color.objects.values_list("name",flat=True).distinct())

def get_all_memory_sizes() -> list[str]:
    return list(MemorySize.objects.values_list("size",flat=True).distinct())

def get_all_brands() -> list[str]:
    return list(Brand.objects.values_list("name",flat=True).distinct())
    
def get_all_models() -> list[str]:
    return list(Phone.objects.values_list("model",flat=True).distinct())

