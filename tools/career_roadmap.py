import os
from dotenv import load_dotenv
from agents import function_tool, AsyncOpenAI, OpenAIChatCompletionsModel

load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")

if not gemini_api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")


external_client = AsyncOpenAI(api_key=gemini_api_key, base_url=base_url)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", openai_client=external_client
)

@function_tool
async def get_career_roadmap():
    try:
        prompt = (
            f"I'm interested in becoming a {input['career_field']}.\n"
            "Please provide a step-by-step skill roadmap that includes beginner, intermediate, and advanced level skills.\n"
            "Format the response clearly using bullet points or numbered steps."
        )
        
        response = await external_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        
        output = response.choices[0].message.content
        
        return {
            "skill_roadmap": output.strip()
        }
        
    except Exception as e:
        print("❌ Exception in get_career_roadmap tool:", str(e))
        return {
            "error": f"❌ Exception in get_career_roadmap tool: {str(e)}"
        } 