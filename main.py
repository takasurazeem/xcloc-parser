import openai
from api_keys import *
from json_retriever import retrive_json

json_data = retrive_json('path')

openai.api_key = f"{OPEN_AI_KEY}"

# Define the prompt to be used with ChatGPT
prompt = f"Translate the Target to Urdu carefully reading Note if any: \n{json_data}"
# print(prompt)
# exit(1)
# Call the OpenAI GPT-3 API for translation
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=150,  # Adjust max_tokens as needed
)

# Extract and print the translated text from the API response
translated_text = response.choices[0].text
print("Translated Text (Urdu):")
print(translated_text)