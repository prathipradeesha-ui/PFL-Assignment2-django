from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        Post.objects.create(
            title="Smart Campus Monitoring System",
            author="Praathi",
            category="Internet of Things",
            content="A smart campus monitoring project."
        )

        Post.objects.create(
            title="AI Student Assistant",
            author="Prathi",
            category="Artificial Intelligence",
            content="An AI assistant for students."
        )

        Post.objects.create(
            title="Student Expense Tracker",
            author="Praathi",
            category="Software Engineering",
            content="A system for tracking student expenses."
        )

    def test_homepage_loads(self):
        response = self.client.get(
            reverse("home")
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_homepage_shows_latest_three_posts(self):
        response = self.client.get(
            reverse("home")
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            len(response.context["posts"]),
            3
        )

    def test_search_works(self):
        response = self.client.get(
            reverse("home"),
            {
                "q": "Internet of Things"
            }
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            len(response.context["posts"]),
            1
        )

        self.assertEqual(
            response.context["posts"][0].title,
            "Smart Campus Monitoring System"
        )

    def test_create_page_loads(self):
        response = self.client.get(
            reverse("create_post")
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_create_post(self):
        response = self.client.post(
            reverse("create_post"),
            {
                "title": "New Student Project",
                "author": "Test Student",
                "category": "Software Engineering",
                "content": "Test project content."
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertTrue(
            Post.objects.filter(
                title="New Student Project"
            ).exists()
        )

    def test_post_detail_page(self):
        post = Post.objects.first()

        response = self.client.get(
            reverse(
                "post_detail",
                args=[post.id]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Smart Campus Monitoring System"
        )
