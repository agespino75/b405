import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

from langchain.memory import ChatMessageHistory
l
history = ChatMessageHistory()

history.add_user_message("hi!")

history.add_ai_message("whats up?")

my_chat_memory = history.messages

print("\n----------\n")

print("Chat Memory:")

print("\n----------\n")
print(my_chat_memory)

print("\n----------\n")