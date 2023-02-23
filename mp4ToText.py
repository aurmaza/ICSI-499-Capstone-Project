from moviepy.editor import VideoFileClip
import speech_recognition as speech
import time


video = "Siliconvalley4u mission.mp4"
videoFile = VideoFileClip(video)
audio = videoFile.audio
temp = 'temp.wav'

audio.write_audiofile(temp)

time.sleep(3)


recognizer = speech.Recognizer()
with speech.AudioFile('temp.wav') as source:
    audioData = recognizer.record(source)

text = recognizer.recognize_google(audioData)

print(text)
