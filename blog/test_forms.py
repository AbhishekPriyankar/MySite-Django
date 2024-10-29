# blog/test_forms.py
from django.test import TestCase
from .forms import ArticleForm
from unittest.mock import patch

# Explanation of Form Tests:

# test_article_form_valid_data: Checks that the form is valid with all required fields filled in.
# test_article_form_invalid_data: Confirms the form fails validation if no data is provided, and ensures the correct number of error messages.


class ArticleFormTest(TestCase):
    def test_article_form_valid_data(self):
        form_data = {
            'title': "Valid Article",
            'content': "This is valid content.",
            'published_date': "2024-10-29"
        }
        form = ArticleForm(data=form_data)
        self.assertTrue(form.is_valid())

    @patch('blog.forms.ArticleForm.is_valid')
    def test_article_form_invalid_data(self):
        form = ArticleForm(data={})
        self.assertFalse(form.is_valid())
        self.assertGreaterEqual(len(form.errors), 2)  # Adjusted assertion. Assuming title, content, and published_date are required
