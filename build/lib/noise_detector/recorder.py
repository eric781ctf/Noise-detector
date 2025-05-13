import sounddevice as sd
import soundfile as sf

def record_audio(filename: str, duration: int):
    samplerate = 44100
    print(f"Recording {duration} seconds...")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, audio, samplerate)