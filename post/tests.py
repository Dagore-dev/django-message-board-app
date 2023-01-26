from django.test import TestCase
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='This is a post')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_text_content = post.text
        self.assertEqual(expected_text_content, 'This is a post')
