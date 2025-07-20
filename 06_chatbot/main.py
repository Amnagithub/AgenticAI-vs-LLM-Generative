import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI
from agents.run import RunConfig
import chainlit as cl
from typing import cast

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Gemini API Key is not set pass this in .env file.")

@cl.on_chat_start
async def chat_start():

    external_client= AsyncOpenAI(
        api_key= gemini_api_key,
        base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model= "gemini-2.0-flash",
        openai_client= external_client
    )

    config = RunConfig(
        model= model,
        model_provider= external_client,
        tracing_disabled= True,
    )
    """
    set up the chat session when a user connects.
    """
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat history",[])
    cl.user_session.set("config",config)
    agent:Agent = Agent(name = "Assistant" ,
        instructions= "you are a helpful assistant",
        model = model)
    cl.user_session.set("agent",agent)
    
    await cl.Message(content="Welcom to the chat session! How can I help you today?").send()

@cl.on_message
async def main (message: cl.Message):
    """ process incoming messages and generate responses."""
    msg = cl.Message(content="Thinking....")
    await msg.send()

    agent:Agent= cast (Agent,cl.user_session.get("agent"))
    config :RunConfig= cast (RunConfig,cl.user_session.get("config"))

    history = cl.user_session.get("chat_history") or []
    history.append({"role":"user","content":message.content})

    try:
        print("\n [CALLING_AGENT_WITH_CONTEXT]\n",history,"\n")
        result=Runner.run_sync(starting_agent=agent,input=history,run_config=config)
    
        response = result.final_output

        # Update the thinking message with the actual response
        msg.content = response
        await msg.update()

        #update the session with the new history,
        cl.user_session.set("chat_history",result.to_input_list())

        #log the interaction
        print(f"User:{message.content}")
        print(f"Assistant:{response}")
    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")


