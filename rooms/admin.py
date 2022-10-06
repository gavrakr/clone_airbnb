from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    
    """ Item Admin Definition  """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"classes": ("collapse",), "fields" : ("name", "description", "country", "address", "price")},
        ),
        (
            "Time",
            {"classes": ("collapse",), "fields" : ("check_in", "check_out", "instance_book")},
        ),
        (
            "More About the Space",
            {"classes": ("collapse",), "fields" : ("amenities", "facilities", "house_rules")},
        ),
        (
            "Last Details",
            {"fields" : ("host",)},
        ),
    )

    #ordering = ("name", "price", "bedrooms")

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instance_book",
        "count_amenities",
        "count_photos",
    )

    list_filter = (
        "instance_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("city", "host__username")

    filter_horizontal = ("amenities", "facilities", "house_rules",)

    def count_amenities(self, obj):
        return obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()

    count_amenities.short_description = "amenities"
    count_photos.short_description = "photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition """