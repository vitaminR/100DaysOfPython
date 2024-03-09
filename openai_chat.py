import aiohttp
import asyncio
from dotenv import load_dotenv
import os

# 0. Load environment variables and configure the OpenAI API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise Exception("OPENAI_API_KEY is not set in the environment variables.")


# 1. Define a custom exception for handling errors related to the OpenAI API
class OpenAIError(Exception):
    """Custom exception class for OpenAI API errors."""


# 2. Define the OpenAIChat class for interacting with the OpenAI API
class OpenAIChat:
    # 2.1 Initialization
    def __init__(self, assistant_id):
        self.assistant_id = assistant_id
        self.session = None  # Session will be initialized in create method

    # 2.2 Asynchronous class method for creating an instance with a session
    @classmethod
    async def create(cls, assistant_id):
        instance = cls(assistant_id)
        instance.session = aiohttp.ClientSession()  # Correctly create the session
        return instance

    # 2.3 Create an assistant
    async def create_assistant(self, name, instructions, tools=None):
        """
        Asynchronously creates an assistant with the specified characteristics.
        """
        headers = {"Authorization": f"Bearer {openai.api_key}"}
        payload = {
            "name": name,
            "model": "gpt-4-turbo-preview",
            "instructions": instructions,
            "tools": tools if tools else [],
        }
        response = await self.session.post(
            "https://api.openai.com/v1/assistants", headers=headers, json=payload
        )
        if response.status != 200:
            raise OpenAIError("Failed to create assistant")
        response_json = await response.json()
        return response_json

    # 2.4 Create a thread for interaction
    async def create_thread(self):
        """
        Creates a thread to start a sequence of interactions (conversations).
        """
        headers = {"Authorization": f"Bearer {openai.api_key}"}
        response = await self.session.post(
            f"https://api.openai.com/v1/assistants/{self.assistant_id}/threads",
            headers=headers,
        )
        if response.status != 200:
            raise OpenAIError("Failed to create thread")
        response_json = await response.json()
        return response_json

    # 2.5 Post a message to a thread
    async def post_message(self, thread_id, message_content):
        """
        Posts a message to the specified thread.
        """
        headers = {"Authorization": f"Bearer {openai.api_key}"}
        payload = {
            "assistant_id": self.assistant_id,
            "thread_id": thread_id,
            "messages": [{"role": "user", "content": message_content}],
        }
        response = await self.session.post(
            "https://api.openai.com/v1/threads/messages", headers=headers, json=payload
        )
        if response.status != 200:
            raise OpenAIError("Failed to post message")
        response_json = await response.json()
        return response_json

    # 2.6 Fetch messages from a thread
    async def fetch_messages(self, thread_id):
        """
        Retrieves all messages from the specified thread.
        """
        headers = {"Authorization": f"Bearer {openai.api_key}"}
        response = await self.session.get(
            f"https://api.openai.com/v1/threads/{thread_id}/messages", headers=headers
        )
        if response.status != 200:
            raise OpenAIError("Failed to fetch messages")
        response_json = await response.json()
        return response_json

    # 2.7 Close the session
    async def close(self):
        """Closes the aiohttp session."""
        await self.session.close()


# Example usage:
# async def main():
#     chat = await OpenAIChat.create("your-assistant-id")
#     try:
#         # Example: Create an assistant
#         assistant = await chat.create_assistant("Assistant Name", "Instructions")
#         print(assistant)
#     finally:
#         await chat.close()
#
# asyncio.run(main())
