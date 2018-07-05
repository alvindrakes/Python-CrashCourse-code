import unittest
from survey import AnnonymousSurvey

class TestAnnonymousSurvey(unittest.TestCase):
    """Tests for the class AnoymousSurvey.py"""

    def setUp(self):
        """
        create a survey and a set of responses for use in all test methods
        """

        question = "What language did you first learn to speak?"
        self.my_survey = AnnonymousSurvey(question)
        self.responses = ['English', 'Mandarin', 'Malay']

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_reponses(self):
        """test that three individual responsesare stored properly"""
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()