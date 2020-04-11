import string
import speech

while True:
    print("talk :")
    phrase=speech.input()
    print(f"You have just said : {phrase}")
    #if you want to turn off then say goodbye
    if phrase.lower()=="goodbye":
        break