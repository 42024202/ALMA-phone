from __future__ import annotations
from rest_framework import serializers
from promotion.models.banner import Banner, BannerImage


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ['id', 'image']


class BannerSerializer(serializers.ModelSerializer):
    images = BannerImageSerializer(many=True, read_only=True)

    class Meta:
        model = Banner
        exclude = ["is_active"]

