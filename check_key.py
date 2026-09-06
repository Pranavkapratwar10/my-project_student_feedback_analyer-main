import os
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY")
print("API Key detected:", api_key is not None)

genai.configure(api_key=api_key)
