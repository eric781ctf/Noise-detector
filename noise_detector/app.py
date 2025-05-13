import os
import base64
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, request, render_template
import soundfile as sf
from noise_detector.recorder import record_audio
from noise_detector.analyzer import analyze_audio

# 指定 template 和 static 資料夾
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, "..", "templates")
static_dir = os.path.join(base_dir, "..", "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

def generate_waveform_image(filename):
    data, samplerate = sf.read(filename)

    # 如果是立體聲，取第一軌
    if len(data.shape) > 1:
        data = data[:, 0]

    time_axis = np.linspace(0, len(data) / samplerate, num=len(data))

    fig, ax = plt.subplots(figsize=(8, 2.5))
    ax.plot(time_axis, data, linewidth=0.8, color='dodgerblue')
    ax.set_title("Waveform")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # 移除多餘邊距
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')  # tight 會再幫你裁切空白
    buf.seek(0)
    plt.close(fig)  # 關閉圖表以節省資源
    return base64.b64encode(buf.getvalue()).decode("utf-8")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    waveform = None
    if request.method == "POST":
        duration_str = request.form.get("duration", "5")
        duration = int(duration_str)
        filename = os.path.join(static_dir, "web_recording.wav")
        record_audio(filename, duration)
        result = analyze_audio(filename)
        waveform = generate_waveform_image(filename)
    return render_template("result.html", result=result, waveform=waveform)

if __name__ == "__main__":
    app.run(debug=True)
