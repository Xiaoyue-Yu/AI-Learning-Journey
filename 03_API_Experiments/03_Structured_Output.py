import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# 1. Load the environment variables
load_dotenv()

# 2. Initialize the OpenRouter client (The clean way, instead of raw requests!)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def main():
    print("Requesting JSON data from OpenRouter...")

    # 3. Create the chat completion request
    response = client.chat.completions.create(
        model="qwen/qwen3.6-plus-preview:free", # Using the chosen free model
        response_format={"type": "json_object"}, # Forces JSON output
        messages=[
            {
                "role": "user",
                "content": "Return ONLY valid JSON with keys 'city' as a string and 'temp_c' as an integer. Example city: Pittsburgh."
            }
        ]
    )

    # 4. Extract the raw text content returned by the AI
    raw_text = response.choices[0].message.content
    print("\n--- Raw AI Output (String) ---")
    print(raw_text)

    # 5. Parse the string into a real Python Dictionary
    try:
        data_dict = json.loads(raw_text)
        
        print("\n--- Parsed Python Dictionary ---")
        print(json.dumps(data_dict, indent=2))
        
        # 🌟 THE "AHA" MOMENT: You can now use the data programmatically!
        city_name = data_dict.get('city')
        temperature = data_dict.get('temp_c')
        
        print(f"\n✅ Success! The AI says the temperature in {city_name} is {temperature}°C.")
        print("Now you can feed this variable into a database or a data analysis pipeline!")

    except json.JSONDecodeError:
        print("\n❌ Error: The AI did not return a valid JSON format.")

if __name__ == "__main__":
    main()