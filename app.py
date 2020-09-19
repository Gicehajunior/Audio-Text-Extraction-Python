import extractSpeech

# variable declarations
videoClip = "Khalid - Young Dumb & Broke (Official Music Video).mp4"
audioClip = ""

# class instance
speechExtract = extractSpeech.SpeechExtraction(videoClip)

# video to audio conversion
audioClip = speechExtract.convertVideoCliptoMp3()

#recognize audio
speechExtract.recognizeAudio()

# extract audio text
speechExtract.exportAudioTextToTextFile()





