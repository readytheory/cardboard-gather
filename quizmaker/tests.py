from django.test import TestCase, RequestFactory
from django.test import Client
from django_webtest import WebTest


from .forms import NewQuizForm

from .views import create_interactive

from .models import Quiz


class CreateQuiz(WebTest):
    def setUp(self):
        self.req_factory = RequestFactory()
        self.client = Client()

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
        quizdata = {'name' : 'bellyitcher_stub' }
        response = self.client.post("/quizmaker/create", quizdata)
        self.assertEqual(response.status_code, 301)

    def test_quiz_from_form_gets_saved(self) :
        ''' 
        setup: confirm there are no objects with a given name
        exercise:         add one
        assert: there is one objec of that name
        '''
        newquiz = Quiz
        quizname  = 'ufr osop ois h'
        newquiz.name = quizname
        quizdata = {'name' : quizname }
        matches = Quiz.objects.filter(name = quizname)
        self.assertEqual(len(matches), 0)
        response = self.client.post("/quizmaker/create", quizdata)
        self.assertEqual(response.status_code, 301)
        matches = Quiz.objects.filter(name = quizname)
        self.assertEqual(len(matches), 1)

