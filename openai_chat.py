import openai
import aiohttp
import asyncio
from dotenv import load_dotenv
import os


# 1. Custom Exception for handling OpenAI API errors
class OpenAIError(Exception):
    """A custom exception class to handle specific OpenAI API errors."""


# 2. OpenAIChat Class Definition
class OpenAIChat:
    # 2.1 Initialization
    def __init__(self, assistant_id):
        """
        Initializes the OpenAIChat class with an assistant ID and an asynchronous session.
        Parameters:
        - assistant_id (str): The unique identifier for the OpenAI assistant.
        """
        self.assistant_id = assistant_id
        self.session = aiohttp.ClientSession()

    # 2.2 Creating an Assistant
    async def create_assistant(self, name, instructions, tools=None):
        """
        Creates an assistant with specified characteristics.
        Parameters:
        - name (str): The name of the assistant.
        - instructions (str): Instructions for the assistant.
        - tools (list, optional): Tools the assistant can use.
        Returns:
        - JSON response containing assistant details.
        """
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "OpenAI-Beta": "assistants=v1",
        }
        payload = {
            "name": name,
            "model": "gpt-4-turbo-preview",
            "instructions": instructions,
            "tools": tools if tools else [],
        }
        response = await self.session.post(
            "https://api.openai.com/v1/assistants", headers=headers, json=payload
        )
        print(f"Response Status: {response.status}")  # Diagnostic print
        response_json = await response.json()
        print(f"Response Content: {response_json}")  # Diagnostic print
        return response_json

    # 2.3 Creating a Thread
    async def create_thread(self):
        """
        Creates a thread for a sequence of interactions.
        Returns:
        - JSON response containing thread details.
        """
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "OpenAI-Beta": "assistants=v1",
        }
        response = await self.session.post(
            f"https://api.openai.com/v1/assistants/{self.assistant_id}/threads",
            headers=headers,
        )
        print(f"Response Status: {response.status}")  # Diagnostic print
        response_json = await response.json()
        print(f"Response Content: {response_json}")  # Diagnostic print
        return response_json

    # 2.4 Posting a Message
    async def post_message(self, thread_id, message_content):
        """
        Posts a message to a specific thread.
        Parameters:
        - thread_id (str): The thread ID.
        - message_content (str): The message content.
        Returns:
        - JSON response with the assistant's reply.
        """
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "OpenAI-Beta": "assistants=v1",
        }
        payload = {
            "assistant_id": self.assistant_id,
            "thread_id": thread_id,
            "messages": [{"role": "user", "content": message_content}],
        }
        response = await self.session.post(
            "https://api.openai.com/v1/threads/messages", headers=headers, json=payload
        )
        print(f"Response Status: {response.status}")  # Diagnostic print
        response_json = await response.json()
        print(f"Response Content: {response_json}")  # Diagnostic print
        return response_json

    # 2.5 Fetching Messages
    async def fetch_messages(self, thread_id):
        """
        Retrieves all messages from a specified thread.
        Parameters:
        - thread_id (str): The thread ID.
        Returns:
        - JSON response with all messages from the thread.
        """
        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "OpenAI-Beta": "assistants=v1",
        }
        response = await self.session.get(
            f"https://api.openai.com/v1/threads/{thread_id}/messages", headers=headers
        )
        print(f"Response Status: {response.status}")  # Diagnostic print
        response_json = await response.json()
        print(f"Response Content: {response_json}")  # Diagnostic print
        return response_json

    # 2.6 Closing the Session
    async def close(self):
        """Closes the asynchronous HTTP session."""
        await self.session.close()


# 3. Environment Setup and API Key Configuration
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
