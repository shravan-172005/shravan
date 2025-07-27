import sounddevice 
from scipy.io.wavfile import write 

fps = 44100 
duration = <duration in seconds> 

print("recording start") 
recording = sounddevice.rec(int(duration * fps), samplerate=fps, channels=2) 
sounddevice.wait() 
print("recording over") 
write("<output name>.wav", fps, recording)
