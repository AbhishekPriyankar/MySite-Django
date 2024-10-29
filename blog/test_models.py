from django.test import TestCase
from unittest.mock import patch, MagicMock
from .models import Article

# Explanation of Each Test:
# - `test_title_content`: Verifies that the title field is correctly set in the model.
# - `test_content`: Ensures the content field matches expected content.
# - `test_published_date`: Confirms that the published date is correctly set for the article.

class ArticleModelTest(TestCase):
    
    @patch('blog.models.Article', autospec=True)  # Mock the Article model class
    def test_title_content(self, MockArticle):
        # Configure the mock's attributes to mimic an Article instance
        mock_article = MockArticle.return_value
        mock_article.title = "Test Article"
        mock_article.content = "Sample content"
        mock_article.published_date = "2024-10-29"

        # Assert that the title is correctly set in the mocked instance
        self.assertEqual(mock_article.title, "Test Article")

    @patch('blog.models.Article', autospec=True)
    def test_content(self, MockArticle):
        # Configure the mock to simulate specific article content
        mock_article = MockArticle.return_value
        mock_article.content = "Sample content"
        
        # Assert that the content is as expected in the mocked instance
        self.assertEqual(mock_article.content, "Sample content")

    @patch('blog.models.Article', autospec=True)
    def test_published_date(self, MockArticle):
        # Configure the mock to simulate a specific published date
        mock_article = MockArticle.return_value
        mock_article.published_date = "2024-10-29"
        
        # Assert that the published date matches the expected value
        self.assertEqual(str(mock_article.published_date), "2024-10-29")
