# Import Packages
from dotenv import load_dotenv
from utils.modules import *
load_dotenv()  # Load .env file
from openai import OpenAI
import time
def initialize_client():
    """Initialize the OpenAI client."""
    return OpenAI()

def get_or_create_assistant(client, get_premade_assistant, assistant_id=None):
    """Retrieve or create an assistant."""
    if get_premade_assistant:
        assistant = get_assistant(client, assistant_id) # Retrieve Assistant
        print(assistant.name + " is ready to go!")
    else:
        name = "rag_agent"
        description = "A tutor for science students"
        instructions = """You are a virtual assistant helping to QA a brand manual PDF. Your task is to carefully read through the important chunks of PDF to find the information needed to answer the question.
        Please read through the brand manual carefully, looking for any information relevant to answering the question. 
        Be sure to cite the specific pages where you found the information you used to arrive at your answer.
        If the question cannot be answered based on the information provided in the brand manual, say "I could not find enough information in the provided brand manual to answer this question."
        """
        tools = [
            {type: "retrieval"}
        ]
        assistant = create_assistant(client, name, description, instructions) # Create Assistant
        print("New Assistant created with ID: " + assistant.id)
    return assistant

def get_or_create_thread(client, get_previous_thread, thread_id=None):
    """Retrieve or create a thread."""
    if get_previous_thread:
        thread = get_chat(client, thread_id)
        print("Chat retrieved with ID: " + thread.id)
    else:
        thread = start_new_chat(client)
        print("New chat created with ID: " + thread.id)
    return thread

def create_new_thread(client):
    """Create a new thread."""
    thread = start_new_chat(client)
    print("New chat created with ID: " + thread.id)
    return thread

def add_message_and_run_thread(client, assistant, thread, query):
    """Add a message to the thread and run the assistant."""
    new_message = add_message(client, thread, query)
    print(f"Message added: {new_message}")
    run_chat(client, thread, assistant)
    print(f"Run initiated for query: {query}")
    time.sleep(20)

def retrieve_chat_history(client, thread):
    """Retrieve and print the chat history."""
    history = get_messages_in_chat(client, thread)
    messages = history.data[::-1]
    for message in messages:
        print(message.role.upper() + ": " + message.content[0].text.value)

def main():
    client = initialize_client()
    get_premade_assistant = True
    assistant_id_to_use = "asst_1TJkaPLevxkcyhUbeqWQar4b"
    user_queries = [
        "Super pumps",
        "Tristar 950 specification",
    ]

    assistant = get_or_create_assistant(client, get_premade_assistant, assistant_id_to_use)

    for query in user_queries:
        thread = create_new_thread(client)
        time.sleep(3)
        add_message_and_run_thread(client, assistant, thread, query)
        retrieve_chat_history(client, thread)

if __name__ == "__main__":
    main()