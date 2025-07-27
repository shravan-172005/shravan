import importlib 
import audio_and_silence 

importlib.reload(audio_and_silence) 

from audio_and_silence import AudioProcessor 

audio = AudioProcessor("<input file name>", format="<input format>") 
audio.process_audio(min_silence_len=<custom length>, threshold=-60,output_folder="outputs") 
