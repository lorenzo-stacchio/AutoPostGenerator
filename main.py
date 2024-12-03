import os 
from tts_custom.tts_module import generate_audio, SyntheticAudioTypes
from pydub import AudioSegment
from moviepy.editor import *


if __name__=="__main__":
    audio_dir = "audio/"
    video_clips = []
    audio_method = SyntheticAudioTypes.tts_coqui
    audio_path = f"audio/test"
    text = " ".join(open("config/sanji.txt").readlines())
    audio_path = generate_audio(text=text, filename = audio_path, method = audio_method)