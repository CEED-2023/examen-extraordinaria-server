import time
import os
from groq import Groq

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
# MODEL = "gpt-3.5-turbo"
MODEL = "llama3-70b-8192"

client = Groq(
    api_key=GROQ_API_KEY
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


