import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, RunConfig


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")

if not gemini_api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")


external_client = AsyncOpenAI(api_key=gemini_api_key, base_url=base_url)


model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=external_client
)

config = RunConfig(
    model=model, 
    model_provider=external_client, 
    tracing_disabled=True)