from django.test import TestCase
from unittest.mock import patch
from .models import Article

# Explanation of Each Test:
# - `test_title_content`: Verifies that the title field is correctly set in the model.
# - `test_content`: Ensures the content field matches expected content.
# - `test_published_date`: Confirms that the published date is correctly set for the article.

class ArticleModelTest(TestCase):

    @patch('blog.models.Article.save', autospec=True)
    def test_title_content(self, mock_save):
        # Set up the article instance with a mock for the `save` method
        article = Article(title="Test Article", content="Sample content", published_date="2024-10-29")
        # Save the article instance (mocked, so no actual database call is made)
        article.save()
        # Assert that the title is correctly set
        self.assertEqual(article.title, "Test Article")

    @patch('blog.models.Article.save', autospec=True)
    def test_content(self, mock_save):
        # Set up the article instance with sample content
        article = Article(title="Test Article", content="Sample content", published_date="2024-10-29")
        # Save the article instance
        article.save()
        # Check if the content is correctly stored in the article instance
        self.assertEqual(article.content, "Sample content")

    @patch('blog.models.Article.save', autospec=True)
    def test_published_date(self, mock_save):
        # Set up the article instance with a specific published date
        article = Article(title="Test Article", content="Sample content", published_date="2024-10-29")
        # Save the article instance
        article.save()
        # Assert that the published date is correctly set to "2024-10-29"
        self.assertEqual(str(article.published_date), "2024-10-29")
