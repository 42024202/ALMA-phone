from __future__ import annotations
from rest_framework import serializers
from catalog.models.phone import Phone
from storage.models import Stock


class StockVariantSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source="color.name")
    memory_size = serializers.CharField(source="memory_size.size")

    class Meta:
        model = Stock
        fields = ["color", "memory_size", "quantity"]


class PhoneSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.name")
    colors = serializers.SerializerMethodField()
    memory_sizes = serializers.SerializerMethodField()
    frame = serializers.SerializerMethodField()
    variants = StockVariantSerializer(source="stocks", many=True)

    class Meta:
        model = Phone
        fields = ["id", "brand", "model", "phone_version", "price", "colors", "memory_sizes", "frame", "variants"]
    
    def get_colors(self, obj: Phone) -> list[str]:
        """Get available colors for phone"""
        return list(
            obj.stocks.values_list("color__name", flat=True).distinct()
        )

    def get_memory_sizes(self, obj: Phone) -> list[str]:
        """Get available memory sizes for phone"""
        return list(
            obj.stocks.values_list("memory_size__size", flat=True).distinct()
        )

    def get_frame(self, obj: Phone) -> list[str]:
        """Get available frame for phone"""
        return list(
            obj.stocks.values_list("frame__frame_material", flat=True).distinct()
        )

