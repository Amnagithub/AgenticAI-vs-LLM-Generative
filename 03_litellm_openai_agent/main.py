from dotenv import load_dotenv
import os
import rich
from agents import Agent,Runner,set_tracing_disabled,function_tool
from agents.extensions.models.litellm_model import LitellmModel
import litellm
import warnings

warnings.filterwarnings("ignore", category=UserWarning) # Suppress UserWarnings from litellm

litellm.disable_aiohttp_transport = True  # Disable aiohttp transport for litellm

load_dotenv() # Load environment variables from .env file

set_tracing_disabled(disabled=True) # Disable tracing for the agents

gemini_api_key = os.getenv("GEMINI_API_KEY")

@function_tool # Define a function tool for getting weather information

def get_weather(city :str) -> str:
    print(f"[debug]getting weather for {city}")
    return f"The weather in {city} is sunny with a high of 25°C."


agent = Agent(
    name = "Assistant",
    instructions = "you are a helpful assistant.",
    model = LitellmModel(model="gemini/gemini-2.5-flash",api_key = gemini_api_key) 
)

result = Runner.run_sync(agent,"what is the weather of Karachi?")

rich.print(result.final_output)