# blog/test_views.py
from django.test import TestCase
from django.urls import reverse
from .models import Article

# Explanation of Each Test:

# test_view_url_exists_at_desired_location: Confirms the view is accessible at the expected URL.
# test_view_url_accessible_by_name: Verifies the view can be accessed by the named URL pattern.
# test_view_uses_correct_template: Ensures the correct template (article_list.html) is used.
# test_view_displays_article_content: Confirms the expected content (the article’s title and content) appears in the response.

class ArticleListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create test articles
        cls.article = Article.objects.create(
            title="Sample Article",
            content="This is the content of the sample article.",
            published_date="2024-10-29"
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('article_list'))
        self.assertTemplateUsed(response, 'article_list.html')

    def test_view_displays_article_content(self):
        response = self.client.get(reverse('article_list'))
        self.assertContains(response, "Sample Article")
        self.assertContains(response, "This is the content of the sample article.")
