import pytest
import os
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv

from openai_chat import OpenAIChat, OpenAIError


@pytest.fixture
async def chat():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    assistant_id = os.getenv("ASSISTANT_ID")  # Optionally fetch an existing ID
    chat_instance = await OpenAIChat.create(
        assistant_id
    )  # Initialize chat with async create
    yield chat_instance
    await chat_instance.close()


# 1. Test for Missing API Key
def test_missing_api_key():
    os.environ["OPENAI_API_KEY"] = ""
    # Adjust this test based on how your OpenAIChat class handles missing API keys


# 2. Test Assistant Creation (Success)
@pytest.mark.asyncio
async def test_create_assistant_success(chat, mocker):
    mocker.patch(
        "aiohttp.ClientSession.post",
        return_value=MagicMock(
            status=200, json=MagicMock(return_value={"id": "test_assistant_id"})
        ),
    )

    result = await chat.create_assistant("My Assistant", "Helpful instructions")
    assert result["id"] == "test_assistant_id"


# 3. Test Thread Creation (Error)
@pytest.mark.asyncio
async def test_create_thread_error(chat, mocker):
    mocker.patch(
        "aiohttp.ClientSession.post",
        return_value=MagicMock(
            status=401, json=MagicMock(return_value={"error": "Unauthorized"})
        ),
    )

    with pytest.raises(OpenAIError):
        await chat.create_thread()


# 4. Test Message Posting (Success)
@pytest.mark.asyncio
async def test_post_message_success(chat, mocker):
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

    result = await chat.post_message("test_thread_id", "What is the capital of France?")
    assert "Paris" in result["choices"][0]["message"]["content"]


# 5. Test Fetch Messages
@pytest.mark.asyncio
async def test_fetch_messages(chat, mocker):
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

    messages = await chat.fetch_messages("test_thread_id")
    assert len(messages["choices"]) == 2


# 6. Test Session Closure
@pytest.mark.asyncio
async def test_close_session(chat, mocker):
    mocker.patch("aiohttp.ClientSession.close", new_callable=MagicMock)
    await chat.close()
    aiohttp.ClientSession.close.assert_called_once()
