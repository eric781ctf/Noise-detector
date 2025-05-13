# Noise Detector

Noise Detector is a CLI and Flask-based tool for analyzing background noise quality. It allows users to record audio, analyze its properties, and visualize the results.

## Features

- **CLI Tool**: Record and analyze audio directly from the command line.
- **Web Interface**: A user-friendly web interface for recording and analyzing audio.
- **Audio Analysis**: Provides metrics such as RMS (Root Mean Square), Peak, and Silence Ratio.
- **Waveform Visualization**: Displays the waveform of the recorded audio in the web interface.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/noise-detector.git
cd noise-detector
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### CLI

To use the CLI tool, run the following command:
```bash
python -m noise_detector.cli --duration <seconds> --output <filename>
```

- `--duration`: Duration of the recording in seconds (default: 5).
- `--output`: Output filename for the recording (default: `recording.wav`).

Example:
```bash
python -m noise_detector.cli --duration 10 --output my_recording.wav
```

[cli-tool](/README_IMG/run-cli.png)

### Web Interface

To start the web interface, run:
```bash
invoke run-web
```

Then, open your browser and navigate to `http://127.0.0.1:5000`. You can record audio, analyze it, and view the results, including a waveform visualization.

[homepage](/README_IMG/run-web-home.png)
[result](/README_IMG/run-web-result.png)

## Development

### Linting and Formatting

- Lint the code:
  ```bash
  invoke lint
  ```

- Format the code:
  ```bash
  invoke format
  ```

### Running Tests

Run the tests using:
```bash
invoke test
```

### Running the CLI and Web Interface

- Run the CLI:
  ```bash
  invoke run_cli --duration <seconds>
  ```

- Run the web interface:
  ```bash
  invoke run_web
  ```

## Project Structure

```
noise-detector/
├── noise_detector/          # Source code for the project
│   ├── analyzer.py          # Audio analysis logic
│   ├── app.py               # Flask web application
│   ├── cli.py               # CLI implementation
│   ├── recorder.py          # Audio recording logic
│   ├── reporter.py          # CLI report generation
├── templates/               # HTML templates for the web interface
├── static/                  # Static files (CSS, JS, images)
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Project metadata and build configuration
├── Makefile                 # Common tasks for development
└── README.md                # Project documentation
```

## Dependencies

This project uses the following Python libraries:

- [Typer](https://typer.tiangolo.com/) for CLI functionality.
- [Rich](https://rich.readthedocs.io/) for CLI output formatting.
- [Flask](https://flask.palletsprojects.com/) for the web interface.
- [SoundDevice](https://python-sounddevice.readthedocs.io/) for audio recording.
- [SoundFile](https://pysoundfile.readthedocs.io/) for audio file handling.
- [NumPy](https://numpy.org/) and [SciPy](https://scipy.org/) for audio analysis.
- [Matplotlib](https://matplotlib.org/) for waveform visualization.

## Author

Eric WY Chang  
Email: [eric773dfl@gmail.com](mailto:eric773dfl@gmail.com)