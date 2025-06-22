import os
import rich
from dotenv import load_dotenv
from agents  import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI, set_tracing_disabled,set_default_openai_api,set_default_openai_client

load_dotenv()

set_tracing_disabled(disabled=True)  # Disable tracing for the agents

set_default_openai_api("chat_completions")  # Set default OpenAI API provider

gemini_api_key = os.getenv("GEMINI_API_KEY")

client =AsyncOpenAI(
    api_key = gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(client)


agent = Agent(
    name = "Assistant",
    instructions = "you are a helpful assistant.",
    model = "gemini-2.0-flash"
    )

result = Runner.run_sync(agent,"tell me your name?")

rich.print(result.final_output)