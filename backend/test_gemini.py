
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('GEMINI_API_KEY')
model_name = os.environ.get('GEMINI_MODEL')

if not api_key:
    print("No API Key found")
    exit()

print(f"Testing with model: {model_name}")
genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel(model_name)
    response = model.generate_content("Hello, respond with 'OK'")
    print(f"Success: {response.text}")
except Exception as e:
    print(f"Error: {e}")
