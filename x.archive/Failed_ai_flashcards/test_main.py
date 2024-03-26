import unittest
from unittest.mock import patch
from dotenv import load_dotenv
import os

# Assuming your main.py and test_main.py are in the same directory and
# you're running tests from within that directory, otherwise adjust imports as needed.


class TestEnvVariables(unittest.TestCase):
    def test_env_variables_loaded(self):
        """Test if environment variables can be loaded."""
        load_dotenv()  # Assuming .env is in the same directory as this test file
        self.assertIsNotNone(os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY is not set.")
        self.assertIsNotNone(os.getenv("ASSISTANT_ID"), "ASSISTANT_ID is not set.")


from unittest.mock import patch
import unittest

# Import the specific function if main.py is structured to allow it
# from main import fetch_math_problem


class MockOpenAIResponse:
    def __init__(self):
        self.choices = [MockChoice()]


class MockChoice:
    def __init__(self):
        self.text = "Mocked math problem"


class TestOpenAIAPICall(unittest.TestCase):
    @patch("main.openai.Completion.create")  # Adjusted to 'main.'
    def test_fetch_math_problem(self, mock_create):
        """Test fetching a math problem without hitting the actual API."""
        mock_create.return_value = MockOpenAIResponse()

        # It's important to import here if the function fetch_math_problem isn't globally imported
        from main import fetch_math_problem

        result = fetch_math_problem()
        self.assertEqual(result, "Mocked math problem")


if __name__ == "__main__":
    unittest.main()
