"""
import openai

class Summarizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize(self, content):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Možeš koristiti "gpt-4" ako imaš pristup
            messages=[
                {"role": "user", "content": f"Sumiraj sledeći tekst u 3-4 rečenice: {content}"}
            ]
        )
        return completion.choices[0].message['content'].strip()
"""
