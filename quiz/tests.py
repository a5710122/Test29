from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from quiz.models import Question, Choice, User
from django.utils import timezone

class HomePageTest(TestCase):

    def test_quiz_page_template(self):
        response = self.client.get('/quiz/')
        self.assertTemplateUsed(response, 'quiz/index.html')

    def test_quiz_page_returns_correct_html(self):
        response = self.client.get('/quiz/')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>quiz test29</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'quiz/index.html')

    def test_displays_all_list_question(self):
        response = self.client.get('/quiz/add_question')
        Question.objects.create(question_text='Job not Man', pub_date=timezone.now())
        Question.objects.create(question_text='Silver is Man', pub_date=timezone.now())
        response = self.client.get('/quiz/')
        self.assertIn('Job not Man', response.content.decode())
        self.assertIn('Silver is Man', response.content.decode())


       



    
