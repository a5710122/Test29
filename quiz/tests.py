from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from quiz.models import Question, Choice, User


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/quiz')
        self.assertTemplateUsed(response, 'quiz/index.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/quiz')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>quiz test29</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'index.html')
