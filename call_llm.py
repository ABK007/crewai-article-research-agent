from crewai import LLM
import os


# Ensure the GEMINI_API_KEY is set in your environment
os.environ['GEMINI_API_KEY'] = os.getenv("GEMINI_API_KEY")

# Initialize the LLM
gemini_llm = LLM(
    model="gemini/gemini-1.5-pro",  # Specify the desired Gemini model
    api_key=os.environ['GEMINI_API_KEY'],
    temperature=0.5,  # Adjust the temperature as needed
    verbose=True
)