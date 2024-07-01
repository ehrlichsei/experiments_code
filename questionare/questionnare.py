class Questionnaire:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def calculate_score(self):
        total_score = sum(question.score for question in self.questions)
        return total_score
