import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_valid_input(self):
        response = emotion_detector("I am very happy!")
        self.assertIn("joy", response)

    def test_blank_input(self):
        response = emotion_detector("")
        self.assertEqual(response["dominant_emotion"], None)
