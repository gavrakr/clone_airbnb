from django.db import models

class TimeStampModel(models.Model):

    """Time Stamp Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True