class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """pass"""
        self._question = question
        self._responses = []

    def show_question(self):
        print(self._question)

    def store_respense(self, new_response):
        self._responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self._responses:
            print(f"- {response}")
