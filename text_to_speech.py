from gtts import gTTS
import os
def textspeech(mytext):
    mytext = 'Sample subway surfers game wow so cool'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("audiofiles/sample.mp3")


mytext = 'Sample subway surfers game wow so cool'
textspeech(mytext)

'''****************************************************************'''

# from pydub import AudioSegment
#
# def increase_audio_speed(input_file, output_file, speed_factor):
#     # Load the audio file
#     audio = AudioSegment.from_file(input_file,format = "mp3")
#
#     # Increase the speed
#     faster_audio = audio.speedup(playback_speed=speed_factor)
#
#     # Export the result
#     faster_audio.export(output_file, format="mp3")
#
# # Example usage:
# input_file_path = "audiofiles/sample.mp3"
# output_file_path = "audiofiles/sample2.mp3"
# speed_factor = 1.5  # Adjust this value as needed
#
# increase_audio_speed(input_file_path, output_file_path, speed_factor)
# Playing the converted file
'''***********************************************************************'''

#os.system("start audiofiles/sample.mp3")
