
# financial advice using OpenAI API
import requests

openai_api_key = "sk-proj-BLldiuhVnIFSCjp7r3LcT3BlbkFJhp5jXm5uwhWOlVEkD2Lo"

def get_advice(user_input):
    try:
        # POST request to the OpenAI API to generate advice based on the prompt
        response = requests.post(
            "https://api.openai.com/v1/engines/text-davinci-003/completions",
            headers={
                "Authorization": f"Bearer {openai_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": user_input,
                "max_tokens": 200
            }
        )
        data = response.json()
        if 'choices' in data and len(data['choices']) > 0:
            advice = data['choices'][0]['text'].strip()
            return advice
        else:
            return "No advice generated."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
if __name__ == "__main__":
    get_advice()