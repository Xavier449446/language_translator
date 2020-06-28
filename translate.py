import gtts
from textblob import TextBlob
import speech_recognition as sr 
import playsound
org_lang='hi'
dest_lang='en'
r = sr.Recognizer()                                                                               
with sr.Microphone() as source:                                                                       
                 
    r.adjust_for_ambient_noise(source,2) 
    print("Say what to translate :")                                                                     
    audio = r.listen(source,timeout=2)
    print("Processing.....")
aud =r.recognize_google(audio,language=org_lang)
text= TextBlob(aud)
te=str(text.translate(to=dest_lang))
print(te)
speaker = gtts.gTTS(te,lang=dest_lang)
speaker.save('temp.mp3')
playsound.playsound("temp.mp3")