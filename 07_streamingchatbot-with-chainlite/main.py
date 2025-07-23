import os
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI
from agents.run import RunConfig
from typing import cast

load_dotenv()

Gemini_api_key= os.getenv("GEMINI_API_KEY")
if not Gemini_api_key:
    raise ValueError("Gemini API key is not set.")

@cl.on_chat_start
async def chat_start():

    external_client= AsyncOpenAI(
        api_key= Gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model= OpenAIChatCompletionsModel(
        model= "gemini-2.5-flash",
        openai_client=external_client
    )

    config = RunConfig(
        model= model,
        model_provider=external_client,
        tracing_disabled=True
    )

    """
    set up a user session when a user connects.
    """
    # Initialize an empty chat history in the session.
    cl.user_session.set("chat history",[])
    cl.user_session.set("config",config)
    agent:Agent = Agent(name = "Assistant" ,
        instructions= "you are a helpful assistant",
        model = model)
    cl.user_session.set("agent",agent)
    await cl.Message(content="Welcome to the AI Chatbot Assistant! How can I help you today.").send()



@cl.on_message
async def main(message:cl.Message):
    """
    process incoming messages and generate reponses.
    """
    # Retrieve the chat history from the session.
    history = cl.user_session.get("chat history") or []
    # Append the user's message to the history.
    history.append({"role":"user","content":message.content})
    # Create a new message object for streaming
    msg = cl.Message("")
    await msg.send()

    agent:Agent= cast(Agent,cl.user_session.get("agent"))
    config:RunConfig = cast(RunConfig,cl.user_session.get("config"))

    try:
        print("\n[CALLING_AGENT_WITH_CONTEXT]",history,"\n")
        # Run the agent with streaming enabled
        result=Runner.run_streamed(agent,history,run_config=config)

        # Stream the response token by token
        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data,"delta"):
                token=event.data.delta
                await msg.stream_token(token)

        # Append the assistant's response to the history.
        history.append({"role":"user","content":message.content})

        # Update the session with the new history.
        cl.user_session.get("history",history)

        # Optional: Log the interaction
        print(f"User:{message.content}")
        print(f"Assistant:{msg.content}")

    except Exception as e:
        await msg.update(content=f"Error: {str(e)}")
        print(f"Error: {str(e)}")



if __name__ == "__main__":
    main()
