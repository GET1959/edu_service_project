from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from lms.models import Section, Material
from lms.serializers import SectionSerializer, MaterialSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class MaterialCreateAPIView(CreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialListAPIView(ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('section',)
    ordering_fields = ('section', 'title')


class MaterialRetrieveAPIView(RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialUpdateAPIView(UpdateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDestroyAPIView(DestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
