from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import os
from agents.run import RunConfig
import rich 
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/" 
)

agent = Agent(
    name="Resercher",
    instructions="You are a helpful assistant."
)

config = RunConfig(
    model=OpenAIChatCompletionsModel("gemini-2.0-flash",openai_client=client),
    model_provider=client,
    tracing_disabled=True)

result = Runner.run_sync(agent, "Who are you ?why are you here explain ?",run_config=config)

rich.print(result.final_output)
