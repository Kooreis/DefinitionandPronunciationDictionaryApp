from gtts import gTTS
import os

def get_pronunciation(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = json.loads(response.text)
    pronunciation = data[0]['phonetics'][0]['text']
    audio_link = data[0]['phonetics'][0]['audio']
    tts = gTTS(text=pronunciation, lang='en')
    tts.save("pronunciation.mp3")
    os.system("mpg321 pronunciation.mp3")