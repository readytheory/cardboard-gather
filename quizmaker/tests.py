from django.test import TestCase
from django.test import Client

class CreateQuiz(TestCase):

    def test_quiz_create_by_post_not_logged_in_works(self) :
        c = Client()
        response = c.post('/quizmaker/create/', {'quizname' : 'napoleon' })
        assert response.status_code == 200

