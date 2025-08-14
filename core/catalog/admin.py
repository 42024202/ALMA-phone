from django.contrib import admin
from catalog.models.battery import Battery
from catalog.models.brand import Brand
from catalog.models.camera import Camera, CameraModule
from catalog.models.color import Color
from catalog.models.country import CountryOfOrigin
from catalog.models.display import Display
from catalog.models.frame import Frame
from catalog.models.memory_size import MemorySize
from catalog.models.phone import Phone, PhoneImage

# ------------------ Simple models ------------------

@admin.register(Battery)
class BatteryAdmin(admin.ModelAdmin):
    list_display = ('capacity', 'type', 'fast_charging', 'wireless_charging', 'removable')
    list_filter = ('fast_charging', 'wireless_charging', 'removable')
    search_fields = ('type',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    search_fields = ('name',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(CountryOfOrigin)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    list_display = ('display_size', 'display_type', 'refresh_rate')
    search_fields = ('display_size', 'display_type')


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ('frame_material', 'length', 'width', 'height', 'weight')
    search_fields = ('frame_material',)


@admin.register(MemorySize)
class MemorySizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
    search_fields = ('size',)


# ------------------ Camera with modules ------------------

class CameraModuleInline(admin.TabularInline):
    model = CameraModule
    extra = 1


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('phone', 'type', 'resolution', 'features')
    inlines = [CameraModuleInline]
    search_fields = ('type', 'features')


@admin.register(CameraModule)
class CameraModuleAdmin(admin.ModelAdmin):
    list_display = ('camera', 'module_number', 'resolution', 'features')
    search_fields = ('resolution', 'features')

# ------------------ Phone ------------------
# Inline для дополнительных фотографий
class PhoneImageInline(admin.TabularInline):
    model = PhoneImage
    extra = 1

    
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'phone_version', 'price', 'release_year')
    list_filter = ('brand', 'phone_version', 'release_year')
    search_fields = ('model', 'phone_cpu', 'oc_version')
    raw_id_fields = ('brand', 'battery', 'display', 'country_of_origin')
    inlines = [PhoneImageInline]

