import pyttsx3
engine = pyttsx3.init()

usersay=input()
if usersay.lower()=="hi" or usersay.lower()=="hello":
    engine.say("Hola")
    engine.runAndWait()
engine.say("What's your name my lady?")
engine.runAndWait()
print("What's your name? ")
usernm=input()
print("Hello "+usernm)
engine.say("Hello "+usernm)
engine.runAndWait()
engine.say("what are you doing?"+usernm)
engine.runAndWait()
