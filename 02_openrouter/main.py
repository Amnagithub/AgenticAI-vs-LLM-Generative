
from agents import Agent ,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled
from dotenv import load_dotenv
import os
import rich
from rich import pretty

pretty.install()
set_tracing_disabled(disabled=True)

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client= AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

agent= Agent(
    name="AI Student",
    instructions="You are a helpful AI assistant. Answer the user's questions to the best of your ability.",
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free",openai_client=client)
)
result=Runner.run_sync(starting_agent=agent,input="What is Generative AI?")

rich.print(result.final_output)