import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
def callGPT3(filePath="data.txt", systemPrompt="", userPrompt=""):
    client = OpenAI(api_key=api_key)
    with open(filePath, 'r') as f:
        txt = f.read()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": userPrompt + txt},
        ]
    )

    # Extracting the content from response.choices
    content_str = response.choices[0].message.content
    content_dict = json.loads(content_str)

    return content_dict

if __name__ == "__main__":
    sysPrompt = "The following is a conversation with a financial advisor. The advisor is helping the user with financial advice. foramat as json."
    userPrompt = "Generate a financial report for the user. The user is a 25-year working in India with a salery of "
    res = callGPT3(systemPrompt=sysPrompt, userPrompt=userPrompt)
    print(res)
