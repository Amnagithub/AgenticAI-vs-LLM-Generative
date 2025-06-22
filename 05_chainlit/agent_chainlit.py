import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig,set_tracing_disabled


load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/" 
)

agent = Agent(
    name = "AI Asistant",
    instructions = "You are a helpful assistant.",
)

model = OpenAIChatCompletionsModel(model = "gemini-2.0-flash", openai_client = client)

config = RunConfig(
    model = model,
    model_provider = client,
    tracing_disabled = True
)

@cl.on_chat_start

async def start_chat(): # This function is called when the chat starts
    cl.user_session.set("history",[]) # Initialize the user session with an empty history
    await cl.Message(content = "Welcome to the chat ! How can I help you today?").send()

@cl.on_message

async def my_message(msg: cl.Message): # This function is called when a message is received
    

    history = cl.user_session.get("history") # Retrieve the user session history

    history.append({"role": "user", "content" : msg.content}) # Append the user's message to the history

    result = await Runner.run(
        agent,
        input= msg.content,
        run_config = config)

    await cl.Message(content = result.final_output).send()





