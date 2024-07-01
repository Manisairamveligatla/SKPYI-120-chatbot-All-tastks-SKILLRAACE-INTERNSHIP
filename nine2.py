import pyaudio
import wave

FORMAT = pyaudio.paInt16  
CHANNELS = 1              
RATE = 44100              
CHUNK = 1024              


audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording... Press Ctrl+C to stop.")

wf = wave.open("output.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)

try:
    while True:
        data = stream.read(CHUNK)
        wf.writeframes(data)
except KeyboardInterrupt:
    pass
finally:
    print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf.close()
