from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper


class ModelsTests(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="test topic")

        self.redactor = get_user_model().objects.create_user(
            username="test username",
            password="Test1234",
            first_name="test first",
            last_name="test last",
            years_of_experience=2
        )

        self.newspaper = Newspaper.objects.create(
            title="test title",
            topic=self.topic
        )

    def test_topic_str(self):
        self.assertEqual(
            str(self.topic),
            f"{self.topic.name}"
        )

    def test_redactor_str(self):
        self.assertEqual(
            str(self.redactor),
            f"{self.redactor.username} "
            f"({self.redactor.first_name} {self.redactor.last_name})"
        )

    def test_newspaper_str(self):
        self.assertEqual(str(self.newspaper),
                         f"{self.newspaper.title} ({self.newspaper.topic})")

    def test_create_redactor_with_years_of_experience(self):
        username = "test username"
        password = "Test1234"
        years_of_experience = 2

        self.assertEqual(self.redactor.username, username)
        self.assertTrue(self.redactor.check_password(password))
        self.assertEqual(self.redactor.years_of_experience,
                         years_of_experience)

    def test_redactor_get_absolute_url(self):
        self.assertEqual(self.redactor.get_absolute_url(), "/redactors/1/")
