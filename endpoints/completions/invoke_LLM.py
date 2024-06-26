import time
import os
from groq import Groq
from g4f.client import Client

# MODEL = "gpt-3.5-turbo"
MODEL = "llama3-70b-8192"

api_key=os.environ.get("GROQ_API_KEY")

client = Groq(
    api_key=api_key,
)

def call_LLM(chat_completion, max_retries=5, delay=1):
    retries = 0
    while retries < max_retries:
        result = chat_completion.choices[0].message.content
        if result != "":
            return result
        retries += 1
        time.sleep(delay)
    raise Exception("Max retries reached")

def invoke_LLM(messages):
    chat_completion = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return call_LLM(chat_completion)


