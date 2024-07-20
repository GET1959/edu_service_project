from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Section, Material
from users.models import User


class MaterialTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@sky.pro")
        self.section = Section.objects.create(
            title="Знакомство с языком Python",
            description="Общие сведения о языке, установка начало работы.",
        )
        self.material = Material.objects.create(
            title="Основы Python",
            content="Общие сведения о языке, установка начало работы.",
            section=self.section,
        )
        self.client.force_authenticate(user=self.user)

    def test_material_retrieve(self):
        url = reverse("lms:material-retrieve", args=(self.material.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.material.title)

    def test_material_create(self):
        url = reverse("lms:material-create")
        data = {"title": "Python: переменные, списки, словари",
                "content": "Работа с переменными, списками, словарями", }
        response = self.client.post(url, data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Material.objects.all().count(), 2)

    def test_material_update(self):
        url = reverse("lms:material-update", args=(self.material.pk,))
        data = {"title": "Python: переменные, списки, словари, кортежи"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Python: переменные, списки, словари, кортежи")

    def test_material_delete(self):
        url = reverse("lms:material-delete", args=(self.material.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Material.objects.all().count(), 0)
