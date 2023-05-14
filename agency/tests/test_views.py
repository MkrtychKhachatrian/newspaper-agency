from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


REDACTOR_LIST_URL = reverse("agency:redactor-list")
REDACTOR_CREATE_URL = reverse("agency:redactor-create")


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test username",
            password="test1234",
            years_of_experience=2
        )
        self.client.force_login(self.user)

        get_user_model().objects.create(
            username="redactor1",
            password="password1",
            years_of_experience=1,
        )
        get_user_model().objects.create(
            username="redactor2",
            password="password2",
            years_of_experience=3,
        )

    def test_create_redactor(self):
        form_data = {
            "username": "new.user",
            "password1": "testpass123",
            "password2": "testpass123",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": 4
        }

        self.client.post(REDACTOR_CREATE_URL, data=form_data)

        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience,
                         form_data["years_of_experience"])

    def test_retrieve_redactors(self):
        response = self.client.get(REDACTOR_LIST_URL)
        drivers = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["redactor_list"]),
                         list(drivers))
        self.assertTemplateUsed(response, "agency/redactor_list.html")
