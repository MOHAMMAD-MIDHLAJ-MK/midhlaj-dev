from django.test import TestCase
from django.urls import reverse


class SkillsPageTests(TestCase):
    def test_skills_page_renders_successfully(self):
        response = self.client.get(reverse("skills"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/skills.html")
