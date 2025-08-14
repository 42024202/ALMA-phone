from catalog.catalog_services.phones_logic import get_all_phones
from catalog.catalog_services.catalog_filters import get_all_colors, get_all_memory_sizes, get_all_brands
from promotion.promotion_services.banner_logic import get_main_page_banners, get_banners_images
from promotion.promotion_serializers.banner_serializers import BannerSerializer
from catalog.catalog_serializers.catalog_serializer import PhoneSerializer


def get_catalog_page_data() -> dict[str, list[dict] | dict [str, list[str]]]:
    banners_qs = get_banners_images(get_main_page_banners())
    banners = BannerSerializer(banners_qs, many=True).data

    phones_qs = get_all_phones()
    phones = PhoneSerializer(phones_qs, many=True).data

    filters = {
        "colors": get_all_colors(),
        "memory_sizes": get_all_memory_sizes(),
        "brands": get_all_brands()
    }

    return {
        "banners": banners,
        "phones": phones,
        "filters": filters
    }

