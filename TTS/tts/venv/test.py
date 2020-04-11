import webbrowser
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

def optionA():

    voice.say("Opening BHP site")
    url = 'https://bhp.service-now.com/nav_to.do?uri=%2Fhome.do%3F'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

    # MacOS
    #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    # Windows
    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'


    voice.runAndWait()


def optionB():
    voice.say("you have selected option B")
    voice.runAndWait()


def optionC():
    voice.say("you have selected option C")
    voice.runAndWait()

try:
    while True:
        with sr.Microphone() as source:
            print("Speak :")
            r.adjust_for_ambient_noise(source)
            #r.pause_threshold = 0.5 # seconds of non-speaking audio before a phrase is considered complete...
            #r.energy_threshold = 900  # minimum audio energy to consider for recording...
            #r.phrase_threshold = 0.1  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
            #r.non_speaking_duration = 0.2  # seconds of non-speaking audio to keep on both sides of the recording
            audio = r.listen(source)
            your_speech=r.recognize_google(audio)

            #checking of available options for the inputed speech............
            if your_speech.upper() in "OPEN BHP":
                optionA()
                break


            # Looping out from the system............
            if (r.recognize_google(audio).upper()) in "DONE":
                voice.say("Thank You, Please interact next time ")
                voice.runAndWait()
                break
            else:
                print("Worked!")


        try:
            print(f"You have said :{r.recognize_google(audio)}")
            text_from_file = r.recognize_google(audio)
            #voice = pyttsx3.init()
            voice.say(text_from_file)
            voice.runAndWait()
        except:
            pass
except Exception as e:
    text="Not recognized, Please try next time"
    voice.say(text)
    voice.runAndWait()
    print(text)