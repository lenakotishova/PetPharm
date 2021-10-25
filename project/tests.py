from django.test import TestCase, Client
from project import models
from project.models import Medicine
import ddt
from unittest import mock
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your tests here.


class MedicineTestCases(TestCase):

    def setUp(self):
        super(MedicineTestCases, self).setUp()
        self.client = Client()
        self.user = models.User()
        self.user.save()

    def test_Medicine_create_returns_200(self):
        data = {'title': 'title', 'body': 'body', 'SUPPLIED_TYPE': 'Таблетки'}
        response = self.client.post('/create/', data)
        self.assertEqual(response.status_code, 200)

    def registration(self):
        self.register.user.create()
        self.assertIn(self.user)


