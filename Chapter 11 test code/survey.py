class AnnonymousSurvey():
    """Collect anonymous answers to a survey question"""

    def __init__(self, question):
        """store a question, and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_questions(self):
        """show the survey questions"""
        print(self.question)

    def store_responses(self, new_response):
        """store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all the responses that have been given"""
        print("Survey Result: ")
        for response in self.responses:
            print("- " + response)



