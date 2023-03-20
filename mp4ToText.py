from moviepy.editor import VideoFileClip
import speech_recognition as speech
import time



def mp42Text(video):

    videoFile = VideoFileClip(video)
    audio = videoFile.audio
    temp = 'SampleFiles/temp.wav'

    audio.write_audiofile(temp)

    time.sleep(3)

    recognizer = speech.Recognizer()
    with speech.AudioFile('SampleFiles/temp.wav') as source:
        audioData = recognizer.record(source)

    text = recognizer.recognize_google(audioData)

    return text


if __name__ == "__main__":
    video = "SampleFiles/Siliconvalley4u mission.mp4"
    textOfVideo = mp42Text(video)
