from __future__ import annotations
from rest_framework import serializers
from catalog.models.phone import Phone


class MainPhoneSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.name")
    colors = serializers.SerializerMethodField()
    memory_sizes = serializers.SerializerMethodField()

    class Meta:
        model = Phone
        fields = ["id", "brand", "model", "phone_version", "price", "colors", "memory_sizes"]

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

