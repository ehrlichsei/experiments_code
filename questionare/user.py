class User:
    def __init__(self, name):
        self.name = name
        self.completed_questionnaires = []

    def complete_questionnaire(self, questionnaire):
        self.completed_questionnaires.append(questionnaire)
        return questionnaire.calculate_score()
