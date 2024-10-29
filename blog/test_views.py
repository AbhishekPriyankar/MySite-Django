from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from types import SimpleNamespace

class ArticleListViewTest(TestCase):
    """Test suite for the Article List View in the blog application."""

    @classmethod
    def setUpTestData(cls):
        # Define sample article data with explicit fields
        cls.article_data = SimpleNamespace(
            id=1,
            title="Sample Article",
            content="This is the content of the sample article.",
            published_date="2024-10-29"
        )

    @patch('blog.models.Article.objects.all')
    def test_view_url_exists_at_desired_location(self, mock_all):
        # Mock the query to return our sample article data
        mock_all.return_value = [self.article_data]
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    @patch('blog.models.Article.objects.all')
    def test_view_url_accessible_by_name(self, mock_all):
        # Mock the database call to simulate one article
        mock_all.return_value = [self.article_data]
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)

    @patch('blog.models.Article.objects.all')
    def test_view_uses_correct_template(self, mock_all):
        # Use mock data to simulate articles
        mock_all.return_value = [self.article_data]
        response = self.client.get(reverse('article_list'))
        self.assertTemplateUsed(response, 'article_list.html')

    @patch('blog.models.Article.objects.all')
    def test_view_displays_article_content(self, mock_all):
        # Mock the article data to be displayed on the page
        mock_all.return_value = [self.article_data]
        response = self.client.get(reverse('article_list'))
        self.assertContains(response, self.article_data.title)
        self.assertContains(response, self.article_data.content)
