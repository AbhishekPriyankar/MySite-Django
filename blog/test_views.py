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

# This test case validates the functionality of the Article List View in the blog application.
class ArticleListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Define sample data for an article including an ID for URL resolution.
        cls.article_data = {
            'id': 1,  # ID ensures URL reverse works correctly in the template
            'title': "Sample Article",
            'content': "This is the content of the sample article.",
            'published_date': "2024-10-29"
        }
        # Create an actual Article instance for tests that don't use mocking.
        cls.article = Article.objects.create(**cls.article_data)

    # Test that the view is accessible at the specific URL endpoint.
    @patch('blog.models.Article.objects.all')
    def test_view_url_exists_at_desired_location(self, mock_all):
        # Mock the query to return our sample article data.
        mock_all.return_value = [Article(**self.article_data)]
        response = self.client.get('/articles/')
        # Check that the response status is 200, indicating success.
        self.assertEqual(response.status_code, 200)

    # Test that the view can be accessed by using the named URL pattern.
    @patch('blog.models.Article.objects.all')
    def test_view_url_accessible_by_name(self, mock_all):
        # Mock the database call to simulate one article.
        mock_all.return_value = [Article(**self.article_data)]
        # Access the view using the reverse function and the named URL.
        response = self.client.get(reverse('article_list'))
        # Verify the response status is successful.
        self.assertEqual(response.status_code, 200)

    # Test that the correct template is used by the view.
    @patch('blog.models.Article.objects.all')
    def test_view_uses_correct_template(self, mock_all):
        # Use mock data to simulate articles.
        mock_all.return_value = [Article(**self.article_data)]
        response = self.client.get(reverse('article_list'))
        # Assert that the response uses 'article_list.html' template.
        self.assertTemplateUsed(response, 'article_list.html')

    # Test that the view displays article content correctly in the response.
    @patch('blog.models.Article.objects.all')
    def test_view_displays_article_content(self, mock_all):
        # Mock the article data to be displayed on the page.
        mock_all.return_value = [Article(**self.article_data)]
        response = self.client.get(reverse('article_list'))
        # Check that the article's title and content appear in the page content.
        self.assertContains(response, self.article_data['title'])
        self.assertContains(response, self.article_data['content'])
