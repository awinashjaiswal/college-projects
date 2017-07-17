import pyttsx

engine = pyttsx.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-100)
voices=engine.getProperty("voices")
for voice in voices:
    if voice.gender == "female":
        print  engine.setProperty('voice', voice.id)
        break
fr=open("x.txt","r")
engine.say(fr.read())
#print engine.getProperty('voices')
#engine.say('The quick brown fox jumped over the lazy dog.')

engine.runAndWait()