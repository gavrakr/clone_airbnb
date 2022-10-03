from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class RaservationAdmin(admin.ModelAdmin):

    """ Raservation Admin Definition"""

    pass

