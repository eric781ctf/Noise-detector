import typer
from noise_detector.recorder import record_audio
from noise_detector.analyzer import analyze_audio
from noise_detector.reporter import print_report

def main(duration: int = 5, output: str = "recording.wav"):
    """Record and analyze background noise."""
    record_audio(output, duration)
    analysis = analyze_audio(output)
    print_report(analysis)

if __name__ == "__main__":
    import sys
    typer.run(main)
