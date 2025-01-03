from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review

# Register your models here.

class WordFilter(admin.SimpleListFilter):

    title = "Filter by Words!"
    parameter_name = "potato"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "room",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_hosts",
        "room__category",
        "room__pet_friendly",
    )
