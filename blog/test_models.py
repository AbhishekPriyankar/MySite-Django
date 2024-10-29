# blog/test_models.py
from django.test import TestCase
from .models import Article

class ArticleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up an instance of the model for all tests in this class
        cls.article = Article.objects.create(
            title="Test Article",
            content="This is a test article content.",
            published_date="2024-10-29"
        )

    def test_title_content(self):
        # Test to verify the title content
        self.assertEqual(self.article.title, "Test Article")

    def test_content(self):
        # Test to verify the article content
        self.assertEqual(self.article.content, "This is a test article content.")

    def test_published_date(self):
        # Test to check if the published date is set correctly
        self.assertEqual(str(self.article.published_date), "2024-10-29")
