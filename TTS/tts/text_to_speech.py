try:
    import pyttsx3
except ModuleNotFoundError as e:
    print(f"Your system is missing the required package as : {e}")
    print("-"*10)
    print('''tips:
            use pip3 install pywin32 pypiwin32 pyttsx3
                    or
            use pip install pywin32 pypiwin32 pyttsx3''')
    print("-"*10)

text_from_file=""
with open("C:\\Users\\subhendu.a.panda\\Desktop\\TTS\\test.txt","r") as f:
    for word in f:
        text_from_file=text_from_file+word

voice=pyttsx3.init()
voice.say(text_from_file)
voice.runAndWait()