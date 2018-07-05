from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show question and store responses to the question
my_survey.show_questions()
print("Eneter 'q' to quit at any time.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_responses(response)

# show the survey result 
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()