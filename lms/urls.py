from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (SectionViewSet, MaterialCreateAPIView,
                       MaterialDestroyAPIView, MaterialListAPIView,
                       MaterialRetrieveAPIView, MaterialUpdateAPIView)

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", SectionViewSet)

urlpatterns = [
    path("materials/", MaterialListAPIView.as_view(), name="material-list"),
    path("materials/<int:pk>/", MaterialRetrieveAPIView.as_view(), name="material-retrieve"),
    path("materials/create/", MaterialCreateAPIView.as_view(), name="material-create"),
    path("materials/<int:pk>/update/", MaterialUpdateAPIView.as_view(), name="material-update"),
    path("materials/<int:pk>/delete/", MaterialDestroyAPIView.as_view(), name="material-delete"),
]
urlpatterns += router.urls
