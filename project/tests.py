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



    def registration(self):
        self.register.user.create()
        self.user.post('/register/', User)

    def login(self):
        self.user.post('/login/', User)

    def logged_out(self):
        self.user.post('/logout/', User)
