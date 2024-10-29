# blog/test_forms.py
from django.test import TestCase
from unittest.mock import patch
from .forms import ArticleForm

# Explanation
# Decorator Adjustment: The @patch decorator now directly applies to the is_valid method of ArticleForm. We’ve also provided mock_is_valid as the second argument to test_article_form_invalid_data, which @patch requires.
# Mocking: The mock_is_valid.return_value = False line ensures that the form fails validation, simulating missing required data.



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

    def test_article_form_invalid_data(self):
        """Test form with invalid data (empty fields), expecting form to be invalid and contain errors."""
        form = ArticleForm(data={})  # Providing empty data to trigger validation errors
        self.assertFalse(form.is_valid())

        # Print errors to confirm which fields caused validation issues
        print("Form errors:", form.errors)

        # Check if the number of errors matches expected, adjusting for actual required fields
        expected_error_count = 2  # Adjust this to match the actual required fields
        self.assertEqual(len(form.errors), expected_error_count)
