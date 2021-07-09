import os,sys
import speech_recognition as sr

from pydub import AudioSegment

argumentList = sys.argv

path = "/home/acer/transcription/"

orig_song = path + argumentList[1]
dest_song = "/home/acer/transcription/result.wav"

def convert_ogg_to_wav():
    song = AudioSegment.from_ogg(orig_song)
    song.export(dest_song, format="wav")
    
if __name__ == '__main__':
    convert_ogg_to_wav()

r = sr.Recognizer()
with sr.AudioFile(dest_song) as source:
  audio = r.record(source)  # read the entire audio file

  text = r.recognize_google(audio, language = 'ml-IN')

print (text)