# blog/test_views.py
from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from .models import Article


# Explanation of Each Test:

# test_view_url_exists_at_desired_location: Confirms the view is accessible at the expected URL.
# test_view_url_accessible_by_name: Verifies the view can be accessed by the named URL pattern.
# test_view_uses_correct_template: Ensures the correct template (article_list.html) is used.
# test_view_displays_article_content: Confirms the expected content (the article’s title and content) appears in the response.

class ArticleListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test article with a known ID for URL resolution
        cls.article = Article.objects.create(
            title="Sample Article",
            content="This is the content of the sample article.",
            published_date="2024-10-29"
        )

    @patch('blog.models.Article.objects.all')
    def test_view_url_exists_at_desired_location(self, mock_all):
        mock_all.return_value = [Article(**self.article_data)]
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    @patch('blog.models.Article.objects.all')
    def test_view_url_accessible_by_name(self, mock_all):
        mock_all.return_value = [Article(**self.article_data)]
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)

    @patch('blog.models.Article.objects.all')
    def test_view_uses_correct_template(self, mock_all):
        mock_all.return_value = [Article(**self.article_data)]
        response = self.client.get(reverse('article_list'))
        self.assertTemplateUsed(response, 'article_list.html')

    @patch('blog.views.Article.objects.all')
    def test_view_displays_article_content(self, mock_articles_all):
        # Mock the queryset to control output
        mock_articles_all.return_value = [self.article]
        response = self.client.get(reverse('article_list'))
        self.assertContains(response, "Sample Article")
        self.assertContains(response, "This is the content of the sample article.")
