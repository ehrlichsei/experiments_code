class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options
        self.answer = None
        self.score = 0

    def set_answer(self, answer):
        self.answer = answer
        self.calculate_score()

    def calculate_score(self):
        # 根据具体需求定义打分规则
        self.score = self.options.get(self.answer, 0)
