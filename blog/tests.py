from django.test import TestCase
from blog.models import *
from django.utils import timezone
from django.urls import reverse
from blog.forms import CommentForm
from blog.views import blog_index

# models test
class blogTest(TestCase):

    def create_blog(self, title="only a test", body="yes, this is only a test"):
        return Post.objects.create(title=title, body=body, created_on=timezone.now())

    def test_blog_creation(self):
        b = self.create_blog()
        self.assertTrue(isinstance(b, Post))
        self.assertEqual(b.__unicode__(), b.title)

    def test_blog_list_view(self):
        w = self.create_blog()
        url = reverse("project_index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, str(resp.content))

