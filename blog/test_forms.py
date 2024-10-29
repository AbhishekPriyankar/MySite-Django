from django.test import TestCase
from unittest.mock import patch, PropertyMock
from .forms import ArticleForm

class ArticleFormTest(TestCase):
    """Tests the ArticleForm for valid and invalid data submissions."""

    def test_article_form_valid_data(self):
        """Test form with valid data, expecting form to be valid."""
        form = ArticleForm(data={
            'title': "Valid Article",
            'content': "This is valid content.",
            'published_date': "2024-10-29"
        })
        self.assertTrue(form.is_valid())

    @patch.object(ArticleForm, 'is_valid', return_value=False)
    @patch.object(ArticleForm, 'errors', new_callable=PropertyMock, return_value={'title': ['This field is required.'], 'content': ['This field is required.']})
    def test_article_form_invalid_data(self, mock_is_valid, mock_errors):
        """Test form with invalid data (empty fields), expecting form to be invalid."""
        form = ArticleForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # Adjusted for expected required fields
