import unittest


def create_app():
    pass


class TestApp(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.app = None

    def setUp(self):
        create_app()

    def test_app(self):
        self.assertIsNotNone(self.app)


if __name__ == '__main__':
    unittest.main()
