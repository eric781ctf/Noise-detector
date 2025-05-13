from flask import Flask, request, render_template
from noise_detector.recorder import record_audio
from noise_detector.analyzer import analyze_audio

app = Flask(__name__)

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