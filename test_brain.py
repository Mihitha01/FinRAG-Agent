import os
from dotenv import load_dotenv
from google import genai

# 1. Load the secret key from the .env file
load_dotenv()
my_key = os.getenv("GEMINI_API_KEY")

# 2. Initialize the modern Gemini client
client = genai.Client(api_key=my_key)

print("Sending message to Google Gemini...")

# 3. Ask it a simple question using the fast flash model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say 'Hello World, the Gemini brain is online!'"
)

# 4. Print the AI's exact response
print("\nAI Response:")
print(response.text)