import gtts
from textblob import TextBlob
import speech_recognition as sr 
import playsound

r = sr.Recognizer()                                                                               
with sr.Microphone() as source:                                                                       
                 
    r.adjust_for_ambient_noise(source,2) 
    print("Say what to translate :")                                                                     
    audio = r.listen(source,timeout=2)
    print("Processing.....")
aud =r.recognize_google(audio,language="hi")
text= TextBlob(aud)
te=str(text.translate(to='en'))
print(te)
speaker = gtts.gTTS(te,lang='en')
speaker.save('temp.mp3')
playsound.playsound("temp.mp3")