import unittest
from unittest.mock import MagicMock
from openai import OpenAI
from chat_agent import call_ai

class TestCallAI(unittest.TestCase):
    
    def test_call_ai_success(self):
        mock_client = MagicMock(spec=OpenAI)
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Hello from the AI!"
        mock_client.chat.completions.create.return_value = mock_response
        messages = [{"role": "user", "content": "Hi there!"}]
        model_name = "test-model"
        result = call_ai(mock_client, messages, model_name)
        
        self.assertEqual(result, "Hello from the AI!")

    def test_call_ai_exception_handling(self):
        mock_client = MagicMock(spec=OpenAI)
        mock_client.chat.completions.create.side_effect = Exception("Rate limit exceeded")
        messages = [{"role": "user", "content": "Hi"}]
        result = call_ai(mock_client, messages, "test-model")
        
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()