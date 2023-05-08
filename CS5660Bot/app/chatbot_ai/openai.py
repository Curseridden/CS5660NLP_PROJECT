from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot_response(prompt):
    response = openai.Completion.create(
        model="davinci:ft-personal-2023-05-08-05-46-36",
        prompt=prompt,
        temperature=0,
        max_tokens=1
    )
    response_completion_choices = response.get("choices")
    prompt_response = None
    if response_completion_choices and len(response_completion_choices) > 0:
        prompt_response = response_completion_choices[0]["text"]

    return prompt_response.split(" ")[1]