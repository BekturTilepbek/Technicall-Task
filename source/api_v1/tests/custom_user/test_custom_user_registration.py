from http import HTTPStatus

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class CustomUserRegistration(APITestCase):
    def test_register_user_successful(self):
        data = {
            "username": "test_user",
            "password": "testpass5678A",
            "email": "test_user0@gmail.com",
            "role": "moderator"
        }

        response = self.client.post(reverse("api_v1:register"), data, format="json")
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue("access" in response.data)


    def test_register_user_unsuccessful(self):
        data = {
            "username": "test_user",
            "password": "12345678",
            "email": "test_user0@gmail.com",
            "role": "moderator"
        }

        response = self.client.post(reverse("api_v1:register"), data, format="json")
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertTrue("password" in response.data)
