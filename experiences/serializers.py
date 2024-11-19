from rest_framework.serializers import ModelSerializer
from .models import Experience, Perk


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"