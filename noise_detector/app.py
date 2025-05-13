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

    # 單聲道處理
    if len(data.shape) > 1:
        data = data[:, 0]

    time_axis = np.linspace(0, len(data) / samplerate, num=len(data))

    # 設定圖表與繪圖區背景為深黑灰
    fig, ax = plt.subplots(figsize=(10, 3), facecolor='#0d0d0d')
    ax.set_facecolor('#0d0d0d')

    ax.plot(time_axis, data, linewidth=1.0, color='#00BFFF')  # 波形為亮藍色
    ax.set_title("Waveform", fontsize=14, color='white', pad=10)
    ax.set_xlabel("Time (s)", fontsize=12, color='white')
    ax.set_ylabel("Amplitude", fontsize=12, color='white')
    ax.grid(True, linestyle='--', alpha=0.3)

    # 軸樣式設定
    ax.tick_params(colors='white', labelsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')

    plt.tight_layout()

    # 輸出 PNG 並保留背景色
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight', facecolor=fig.get_facecolor())
    buf.seek(0)
    plt.close(fig)
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
