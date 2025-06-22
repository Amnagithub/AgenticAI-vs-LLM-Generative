import chainlit as cl
from dotenv import load_dotenv

load_dotenv()
@cl.on_chat_start
async def start_chat():
   await cl. Message(content = "Welcome to the chat! How can I assist you today?").send()

@cl.on_message
async def my_message(msg : cl.Message):
    user_input = msg.content
    await cl.Message(content = user_input).send()

