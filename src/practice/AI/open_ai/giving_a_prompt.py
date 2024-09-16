import openai
from apikey import APIKEY
openai.api_key = APIKEY

output = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user',
    'content':'explain how electrons move through conductive and semiconductive materials using electron flow'}]
)

print(output)