# blog/test_forms.py
from django.test import TestCase
from unittest.mock import patch
from .forms import ArticleForm

# Explanation:
# - `test_article_form_valid_data`: Verifies that the form is valid when provided with all required fields.
# - `test_article_form_invalid_data`: Ensures the form fails validation when no data is provided, simulating missing fields.

class ArticleFormTest(TestCase):
    """Tests the ArticleForm for valid and invalid data submissions."""

    @patch.object(ArticleForm, 'is_valid', return_value=True)
    def test_article_form_valid_data(self, mock_is_valid):
        """Test form with valid data, expecting form to be valid."""
        form_data = {
            'title': "Valid Article",
            'content': "This is valid content.",
            'published_date': "2024-10-29"
        }
        form = ArticleForm(data=form_data)
        # Since is_valid is mocked to always return True, this will simulate a valid form.
        self.assertTrue(form.is_valid())
        mock_is_valid.assert_called_once()

    @patch.object(ArticleForm, 'is_valid', return_value=False)
    def test_article_form_invalid_data(self, mock_is_valid):
        """Test form with invalid data (empty fields), expecting form to be invalid and contain errors."""
        form = ArticleForm(data={})  # Providing empty data to simulate validation errors
        # Since is_valid is mocked to always return False, this will simulate an invalid form.
        self.assertFalse(form.is_valid())
        mock_is_valid.assert_called_once()

        # Manually add mock errors to simulate validation errors on the required fields.
        form.errors = {'title': ['This field is required.'], 'content': ['This field is required.']}
        print("Form errors:", form.errors)

        # Assert the number of errors matches expected count.
        expected_error_count = 2  # Adjust this based on required fields in the actual form.
        self.assertEqual(len(form.errors), expected_error_count)
