import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3("WhatsApp Audio 2020-04-20 at 7.27.45 PM.mp3")
sound.export("WhatsApp Audio 2020-04-20 at 7.27.45 PM.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "WhatsApp Audio 2020-04-20 at 7.27.45 PM.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))


'''class fcbarc(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def players(self):
        print("hi iam ", self.name, "and iam", self.age,"yeras old")

    def changeage(self,age):
        self.age = age


guna = fcbarc("messi",32)
zeus = fcbarc("suarez",33)

zeus.players()
guna.players()
guna.changeage(3)'''

        
