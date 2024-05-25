class ErrorSerializer:
    def __init__(self, error):
        self.error = error

    def serialize(self):
        return {
            "title": self.error.title,
            "description": self.error.description
        }