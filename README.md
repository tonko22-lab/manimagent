# SmoLAgents Project

Project for working with LLM models and code tools.

## Requirements

- Python 3.11.8
- Virtual environment (recommended)
- System dependencies for Manim:
  ```bash
  # For Debian/Ubuntu
  sudo apt update
  sudo apt install -y build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
  ```

## Installation

1. Create and activate virtual environment:
```bash
python3.11 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file in the root directory and add your configuration:
```bash
API_KEY=your_api_key_here
```

## Usage

Run the local agent:
```bash
python local_run.py
```

### Visualization

For running algorithm visualizations:
```bash
python -m manim -pql algovis/sliding_window.py SlidingWindowScene
```
