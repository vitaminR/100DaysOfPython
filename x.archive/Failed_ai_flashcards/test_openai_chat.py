import pytest
import os
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv
from openai_chat import OpenAIChat, OpenAIError

# 1. Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("ASSISTANT_ID")


# 2. Define a pytest fixture for async setup and teardown
@pytest.fixture
async def chat():
    # 2.1 Check if the OPENAI_API_KEY is set
    if not api_key:
        raise Exception("OPENAI_API_KEY is not set in the environment variables.")
    # 2.2 Create an instance of OpenAIChat
    chat_instance = await OpenAIChat.create(assistant_id)
    yield chat_instance  # 2.3 Provide the instance to the test
    await chat_instance.close()  # 2.4 Close the instance after the test


# 3. Define your tests using the async pattern
@pytest.mark.asyncio
async def test_create_assistant_success(chat):
    # 3.1 Mock the aiohttp session post method to simulate API call
    with patch(
        "aiohttp.ClientSession.post",
        return_value=MagicMock(
            status=200, json=MagicMock(return_value={"id": "test_assistant_id"})
        ),
    ):
        # 3.2 Call the create_assistant method and await its result
        result = await chat.create_assistant("My Assistant", "Helpful instructions")
        # 3.3 Assert the result as expected
        assert result["id"] == "test_assistant_id"


# Additional tests following the setup provided previously


# 4. Test handling of thread creation error
@pytest.mark.asyncio
async def test_create_thread_error(chat, mocker):
    # 4.1 Mock the session post method to simulate a failing API call
    mocker.patch(
        "aiohttp.ClientSession.post",
        return_value=MagicMock(
            status=401, json=MagicMock(return_value={"error": "Unauthorized"})
        ),
    )
    # 4.2 Attempt to create a thread and expect a specific exception
    with pytest.raises(OpenAIError):
        await chat.create_thread()


# 5. Test successful posting of a message
@pytest.mark.asyncio
async def test_post_message_success(chat, mocker):
    # 5.1 Mock the session post method to simulate a successful message post
    mocker.patch(
        "aiohttp.ClientSession.post",
        return_value=MagicMock(
            status=200,
            json=MagicMock(
                return_value={
                    "choices": [
                        {"message": {"content": "Paris is the capital of France."}}
                    ]
                }
            ),
        ),
    )
    # 5.2 Post a message and verify the response content
    result = await chat.post_message("test_thread_id", "What is the capital of France?")
    assert "Paris" in result["choices"][0]["message"]["content"]


# 6. Test fetching messages from a thread
@pytest.mark.asyncio
async def test_fetch_messages(chat, mocker):
    # 6.1 Mock the session get method to simulate fetching messages
    mocker.patch(
        "aiohttp.ClientSession.get",
        return_value=MagicMock(
            status=200,
            json=MagicMock(
                return_value={
                    "choices": [
                        {"message": {"content": "What is the capital of France?"}},
                        {"message": {"content": "Paris is the capital of France."}},
                    ]
                }
            ),
        ),
    )
    # 6.2 Fetch messages and assert the length of the choices
    messages = await chat.fetch_messages("test_thread_id")
    assert len(messages["choices"]) == 2


# 7. Test closing of the session
@pytest.mark.asyncio
async def test_close_session(chat, mocker):
    # 7.1 Mock the session close method to ensure it gets called
    mocker.patch("aiohttp.ClientSession.close", new_callable=MagicMock)
    # 7.2 Close the chat session and verify the close method was called
    await chat.close()
    aiohttp.ClientSession.close.assert_called_once()
