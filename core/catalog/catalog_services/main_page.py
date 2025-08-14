from __future__ import annotations
from catalog.catalog_services.catalog_filters import get_all_brands
from catalog.catalog_services.phones_logic import get_all_phones
from catalog.catalog_serializers.main_page_serializer import MainPhoneSerializer
from promotion.promotion_services.banner_logic import get_main_page_banners, get_banners_images
from promotion.promotion_serializers.banner_serializers import BannerSerializer 


def main_page_data() -> dict[str, list[dict] | dict [str, list[str]]]:
    banners = BannerSerializer(get_banners_images(get_main_page_banners()), many=True).data
    phones = MainPhoneSerializer(get_all_phones(), many=True).data
    filters = {
        'brands': get_all_brands()
        }
    return {
            'phones': phones,
            'banners': banners,
            'filters': filters
            }

