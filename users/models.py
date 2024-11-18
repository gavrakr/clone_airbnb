from django.db import models
from django.contrib.auth.models import AbstractUser

#### Custom User Models

class User(AbstractUser):

    # Class to Choices
    
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        
    class LanguageChoices(models.TextChoices):
        EN = ("en", "english")
        KR = ("kr", "korean")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Koean won")
        USD = ("usd", "Dollar")

    # Variable
    
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    profile_photo = models.ImageField(blank=True )
    #profile_photo = models.URLField(blank=True )
    name = models.CharField(max_length=150, default="", blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices)
    is_hosts = models.BooleanField(null=True)