import numpy as np
import soundfile as sf

def analyze_audio(filename: str) -> dict:
    data, samplerate = sf.read(filename)

    if len(data.shape) > 1:
        data = data[:, 0]  # 取單聲道

    rms = np.sqrt(np.mean(data**2))
    peak = np.max(np.abs(data))

    frame_length = int(0.02 * samplerate)  # 20ms 每幀
    frame_step = frame_length

    frames = [
        data[i:i+frame_length]
        for i in range(0, len(data) - frame_length + 1, frame_step)
    ]

    energies = np.array([np.sqrt(np.mean(f**2)) for f in frames])
    silence_threshold = 0.02  # 可以依據測試調整
    silence_ratio = np.sum(energies < silence_threshold) / len(energies)

    return {
        "rms": float(rms),
        "peak": float(peak),
        "silence_ratio": float(silence_ratio),
    }
