import speech_recognition as sr
listener = sr.Recognizer()

print('yo')
try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        words = listener.recognize_google(voice)
        print(words)
except:
    pass

