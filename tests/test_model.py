import unittest
from backend.model import YOLOModel

class TestYOLOModel(unittest.TestCase):
    def test_model_loading(self):
        model = YOLOModel()
        self.assertIsNotNone(model.model)

if __name__ == '__main__':
    unittest.main()
