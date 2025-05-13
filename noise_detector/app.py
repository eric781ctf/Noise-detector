from flask import Flask, request, render_template
from noise_detector.recorder import record_audio
from noise_detector.analyzer import analyze_audio
import os

# 明確告訴 Flask 去找上層的 templates 資料夾
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, "..", "templates")

app = Flask(__name__, template_folder=template_dir)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        duration = int(request.form.get("duration", 5))
        filename = "web_recording.wav"
        record_audio(filename, duration)
        result = analyze_audio(filename)
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)