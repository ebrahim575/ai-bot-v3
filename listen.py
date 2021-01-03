import speech_recognition as sr
listener = sr.Recognizer()
while(1):
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            words = listener.recognize_google(voice)
            print(words)
            f = open('output2.txt','a')
            f.write(words + '\n')
            f.close()
    except:
        print('Except executed')
        pass


