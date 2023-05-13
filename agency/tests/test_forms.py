from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Newspaper


REDACTOR_UPDATE_URL = reverse("agency:redactor-update", kwargs={"pk": 1})


class ExperienceValidationTests(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="test username",
            password="test123",
            years_of_experience=2
        )

        self.client.force_login(self.redactor)

    def test_years_of_experience_less_than_0(self):
        response = self.client.post(REDACTOR_UPDATE_URL,
                                    data={"years_of_experience": -1})

        self.assertFormError(response, "form", "years_of_experience",
                             "Years of experience can't be less than 0")

    def test_years_of_experience_more_than_100(self):
        response = self.client.post(REDACTOR_UPDATE_URL,
                                    data={"years_of_experience": 101})

        self.assertFormError(response, "form", "years_of_experience",
                             "You can't be this old :) Years of experience can't be more than 100")


class SearchFormsTests(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Tech")

        self.redactor = get_user_model().objects.create_user(
            username="test username",
            password="Test1234",
            first_name="test first",
            last_name="test last",
            years_of_experience=2
        )

        self.newspaper = Newspaper.objects.create(
            title="Robot Technologies",
            topic=self.topic
        )

    def test_redactors_search_username(self):
        response = self.client.get(
            reverse("agency:redactor-list") + "?username=test username"
        )

        self.assertFalse("user.bob" in str(response.content))

    def test_newspapers_search_robot_technologies(self):
        response = self.client.get(
            reverse("agency:newspaper-list") + "?title=Robot Technologies"
        )

        self.assertFalse("Top 10 Healthiest Foods" in str(response.content))

    def test_topics_search_tech(self):
        response = self.client.get(
            reverse("agency:topic-list") + "?name=Tech"
        )

        self.assertFalse("Education" in str(response.content))
