import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Initialize the OpenRouter client
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

print("Sending request to OpenRouter using Qwen 3.6 Plus Preview...")

# Create the chat completion request
response = client.chat.completions.create(
  model="qwen/qwen3.6-plus-preview:free", 
  messages=[
    {
      "role": "system",
      "content": "You are an experienced academic advisor at the University of Pittsburgh. Your tone is professional, welcoming, and concise."
    },
    {
      "role": "user",
      "content": "Please provide a brief introduction to the University of Pittsburgh, and then highlight the key focus areas and strengths of its Information Science major."
    }
  ]
)

# Print the response
print("\n--- AI Response ---\n")
print(response.choices[0].message.content)
print("\n-------------------\n")