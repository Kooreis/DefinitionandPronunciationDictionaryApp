import json
import requests


def get_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = json.loads(response.text)
    return data[0]['meanings'][0]['definitions'][0]['definition']