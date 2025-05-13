import numpy as np
import soundfile as sf

def analyze_audio(filename: str) -> dict:
    data, samplerate = sf.read(filename)
    rms = np.sqrt(np.mean(data**2))
    peak = np.max(np.abs(data))
    silence_ratio = np.sum(np.abs(data) < 0.01) / len(data)
    return {
        "rms": float(rms),
        "peak": float(peak),
        "silence_ratio": float(silence_ratio),
    }