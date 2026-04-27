
import os
from dotenv import load_dotenv
load_dotenv()

print(f"GEMINI_MODEL: {os.environ.get('GEMINI_MODEL')}")
print(f"GEMINI_FALLBACK_MODELS: {os.environ.get('GEMINI_FALLBACK_MODELS')}")
print(f"FLASK_ENV: {os.environ.get('FLASK_ENV')}")
