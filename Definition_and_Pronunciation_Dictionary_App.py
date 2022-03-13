```python
import json
import requests
from gtts import gTTS
import os

def get_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = json.loads(response.text)
    return data[0]['meanings'][0]['definitions'][0]['definition']

def get_pronunciation(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = json.loads(response.text)
    pronunciation = data[0]['phonetics'][0]['text']
    audio_link = data[0]['phonetics'][0]['audio']
    tts = gTTS(text=pronunciation, lang='en')
    tts.save("pronunciation.mp3")
    os.system("mpg321 pronunciation.mp3")

while True:
    print("1. Get Definition")
    print("2. Get Pronunciation")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        word = input("Enter the word: ")
        print(get_definition(word))
    elif choice == 2:
        word = input("Enter the word: ")
        get_pronunciation(word)
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please choose again.")
```