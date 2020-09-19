# from library
import speech_recognition
import moviepy.editor as moviepy
import os

class SpeechExtraction:
    VideoClipFile = ""
    ConvertedClipFile = "converted.wav"
    audio_path = "converted.wav"
    clip = ""
    audio = ""
    result = ""
    recognized_text_file = ""
    
    ####
    # Class constructor
    #Takes two parameters
    #   -the video clip file path.
    #   -the converted clip file.
    # ####
    def __init__(self, VideoClipFile):
        self.VideoClipFile = VideoClipFile

    ####
    # conversion of the video clip file to an audio file.
    # writes the audio file to path.
    # parameter passed, instance of this class, self.
    ####
    def convertVideoCliptoMp3(self):
        self.clip = moviepy.VideoFileClip(self.VideoClipFile) 
        
        self.clip.audio.write_audiofile(self.audio_path)
        
        return self.clip

    ####
    # Recognizes the audio text from the converted wav file
    # parameter passed,instance of this class, self.
    ####
    def recognizeAudio(self):
        recognizer = speech_recognition.Recognizer() 
        self.audio = speech_recognition.AudioFile(self.audio_path)

        with self.audio as source:
            audio_file = recognizer.record(source)
            
        self.result = recognizer.recognize_google(audio_file)
        
        return self.result

    ####
    #If text file to save audio text recognized, the system creates the text file.
    # Exports audio text to a file.
    ####
    def exportAudioTextToTextFile(self):
        self.result = recognizeAudio()
        self.recognized_text_file = "recognized.txt"
        
        if os.path.exists(self.recognized_text_file):
            pass
        else:
            os.mkdir(self.recognized_text_file)
        
        with open(self.recognized_text_file, mode ='w') as file: 
            file.write("Recognized Speech:") 
            file.write("\n") 
            file.write(self.result) 
            print("ready!")


