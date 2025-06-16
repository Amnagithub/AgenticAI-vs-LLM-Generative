from dotenv import load_dotenv
import os
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,set_tracing_disabled

load_dotenv()
# Load environment variables from .env file
set_tracing_disabled(True)

gemini_api_key=os.getenv("Gemini_API_KEY")

client =AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

agent =Agent(
    name="my agent",
    instructions="you are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)
)

user=input("Enter your question: ")
result= Runner.run_sync(agent,user)
print(result.final_output)



