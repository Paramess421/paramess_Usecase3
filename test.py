# test.py
from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

client = OpenAI(base_url='https://api.groq.com/openai/v1', api_key=os.environ['GROQ_API_KEY'])
r = client.chat.completions.create(
    model='openai/gpt-oss-120b',
    messages=[{'role': 'user', 'content': 'say ok'}],
    max_tokens=10
)
print(r.choices[0].message.content)