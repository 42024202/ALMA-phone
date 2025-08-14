from django.contrib import admin
from .models.banner import Banner, BannerImage


class BannerImageInline(admin.TabularInline):
    model = BannerImage
    extra = 1
    readonly_fields = ('id',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type_of_bunner', 'is_active')
    list_filter = ('type_of_bunner', 'is_active')
    search_fields = ('title', 'description')
    inlines = [BannerImageInline]


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner', 'image')
    search_fields = ('banner__title',)

