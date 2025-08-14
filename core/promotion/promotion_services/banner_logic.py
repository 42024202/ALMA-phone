from __future__ import annotations
from typing import TypeAlias
from django.db.models import QuerySet
from promotion.models.banner import Banner 
from promotion.promotion_constants import BannerTypeChoise


ActiveBanners:TypeAlias = QuerySet[Banner]
MainPageBanners:TypeAlias = QuerySet[Banner]
CatalogBanners:TypeAlias = QuerySet[Banner]
BrandBanners:TypeAlias = QuerySet[Banner]

def active_banners()-> ActiveBanners:
    """Get all active banners"""
    return Banner.objects.filter(is_active=True)

def get_main_page_banners()-> MainPageBanners:
    """Get all active main page banners"""
    return active_banners().filter(type_of_bunner__in=[
            BannerTypeChoise.INDEX_HEAD,
            BannerTypeChoise.INDEX_MIDDLE
                ]
            )

def get_catalog_banners()-> CatalogBanners:
    """Get all active catalog page banners"""
    return active_banners().filter(type_of_bunner=BannerTypeChoise.CATALOG_HEAD)

def get_brand_banner()-> BrandBanners:
    """Get all active brand page banners"""
    return active_banners().filter(type_of_bunner=BannerTypeChoise.BRAND_HEAD)

def get_banners_images(banners: QuerySet[Banner])-> ActiveBanners:
    """Get all related images to banner"""
    return banners.prefetch_related("images")

