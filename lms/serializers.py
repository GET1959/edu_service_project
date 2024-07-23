from rest_framework.serializers import ModelSerializer

from lms.models import Section, Material


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ("id", "title", "description", "materials")


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"
