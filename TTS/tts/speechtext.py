try:
    import pyttsx3
    import speech_recognition as sr
    import pyttsx3
except ModuleNotFoundError as e:
    print(f"Your system is missing the required package as : {e}")
    print("-"*10)
    print('''tips:
            use pip3 install pywin32 pypiwin32 pyttsx3 SpeechRecognition PyAudio
                    or
            use pip install pywin32 pypiwin32 pyttsx3 SpeechRecognition PyAudio''')
    print("-"*10)



text_from_file=""
r = sr.Recognizer()
voice = pyttsx3.init()

try:
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Speak :")
            audio=r.listen(source)
            if (r.recognize_google(audio).upper()) == "GOODBYE":
                print("It's a bye....See you next time")
                break
            else:
                print("Worked!")

            try:
                print(f"You have said :{r.recognize_google(audio)}")
                text_from_file = r.recognize_google(audio)
                voice = pyttsx3.init()
                voice.say(text_from_file)
                voice.runAndWait()
            except:
                pass
except Exception as e:
    print("Not recognized, Please try next time !")