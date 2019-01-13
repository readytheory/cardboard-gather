from django.test import TestCase, RequestFactory
from django.test import Client
from django_webtest import WebTest
from django.urls import reverse
from django.shortcuts import render

import bleach

from .forms import NewQuizForm
from .views import create_interactive
from .models import Quiz

class CreateQuiz(TestCase):

    def setUp(self):
        self.rfactory = RequestFactory()
        self.client = Client()
        self.card1 = { 'id' : 1,
                  'question_text' : 'Which came first?'
                  }
        self.card2 = { 'id' : 2,
                  'question_text' : 'What dinosaur ate most?'}
                  

    def test_get_new_quiz_form_has_field_and_button(self) :
        c = self.client
        resp = c.get('/quizmaker/create/')
        self.assertEqual(resp.status_code, 200)
        content = resp.content
        self.assertTrue( b', hon' in content)
        self.assertTrue( b'<input type="submit"')
        self.assertTrue( b'<input type="text" name="quizname"')

    def test_newquiz_form_validates(self):
        form = NewQuizForm({"name" : "beelzebub"})
        self.assertTrue(form.is_valid())

    def test_submit_new_quiz_redirects(self) :
        c  = self.client
        quizdata = {'quizname' : 'bellyitcher_stub' }
        #        import pdb; pdb.set_trace()
        response = c.post(reverse('quizmaker:quiz_create_from_form_data'), quizdata, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain),1)
        
    def test_quiz_from_form_gets_saved(self) :
        ''' 
        setup: confirm there are no objects with a given name
        exercise:         add one
        assert: there is one object of that name
        '''
        newquiz = Quiz
        quizname  = bleach.clean('ufr osop ois h')
        newquiz.name = quizname
        quizdata = {'quizname' : quizname }
        matches = Quiz.objects.filter(name = quizname)
        self.assertEqual(len(matches), 0)
        response = self.client.post(reverse('quizmaker:quiz_create_from_form_data'),
                                    quizdata, follow=True)
        self.assertEqual(response.status_code, 200)
        matches = Quiz.objects.filter(name = quizname)
        self.assertEqual(len(matches), 1)

    def test_new_quiz_shows_quiz_name(self) :
        quizname  = bleach.clean('ufr osop ois h2')
        matches = Quiz.objects.filter(name = quizname)
        self.assertEqual(len(matches), 0)
        quizdata = {'quizname' : quizname }
        response = self.client.post(reverse('quizmaker:quiz_create_from_form_data'),
                                    quizdata, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(bytes("Quiz name: {}".format(quizname), 'utf-8') in response.content)

    def test_quiz_add_cards_template_shows_cards(self) :
        '''Bypassing the normal workflow and hitting the template directly
with known values, make sure the echoes the questions back.'''
        cards = [self.card1, self.card2]
        quizdata = {'quizname' : 'uho mcuhoface',
                    'cards' : cards }
        req = self.rfactory.post('/')
        response = render(req, 'quizmaker/add_cards_to_quiz.html' , quizdata)
        for card in cards :
            self.assertTrue(bytes(card['question_text'], 'utf-8') in response.content)

        
        
