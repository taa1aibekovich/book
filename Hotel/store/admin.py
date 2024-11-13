from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from .traslation import Hotel


class HotelPhotosInline(admin.TabularInline):
    model = HotelPhotos
    extra = 1


class RoomPhotosInline(admin.TabularInline):
    model = RoomPhotos
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomPhotosInline]


admin.site.register(Room, RoomAdmin)


@admin.register(Hotel)
class ProductAdmin(TranslationAdmin):
    inlines = [HotelPhotosInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(Booking)
