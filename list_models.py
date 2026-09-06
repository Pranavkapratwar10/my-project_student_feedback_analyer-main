import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models(page_size=20)
for m in models:
    if "generate" in m.supported_generation_methods:
        print(m.name)
