import asyncio
import os
from openai_chat import OpenAIChat, OpenAIError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch the assistant ID from environment variables
ASSISTANT_ID = os.getenv("ASSISTANT_ID")


# Ensure to pass the correct assistant ID to the OpenAIChat class instance
async def test_openai_chat():
    # Ensure that the ASSISTANT_ID variable is used instead of the string "ASSISTANT_ID"
    chat = OpenAIChat(assistant_id=ASSISTANT_ID)

    try:
        print("Creating an assistant...")
        assistant = await chat.create_assistant(
            name="Test Assistant", instructions="Answer the user's questions."
        )
        print("Assistant created:", assistant)

        print("\nCreating a thread...")
        thread = await chat.create_thread()
        # Ensure to handle cases where 'id' might not be in the response
        thread_id = thread.get("id", "")
        print("Thread created:", thread)

        # Only proceed if thread_id is present
        if thread_id:
            print("\nPosting a message to the thread...")
            message_content = "What is the capital of France?"
            message = await chat.post_message(thread_id, message_content)
            print("Message posted:", message)

            print("\nFetching messages from the thread...")
            messages = await chat.fetch_messages(thread_id)
            print("Messages fetched:", messages)
        else:
            print("Thread creation failed; no valid thread ID received.")

    except OpenAIError as e:
        print("An error occurred:", e)

    finally:
        print("\nClosing the session...")
        await chat.close()
        print("Session closed.")


if __name__ == "__main__":
    asyncio.run(test_openai_chat())
