# AR Shell Project

Lightweight AR/assistant shell used for launching apps, widgets, and simple AI integrations.

## Requirements

- Python 3.10+ (virtual environment recommended)
- See `requirements.txt` for Python dependencies

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Start the application:

```bash
python main.py
```

## Project layout

- `core/` — core services and managers
- `services/` — individual feature services (detection, translation, etc.)
- `ui/` — UI windows, widgets and animations
- `assets/` — static assets

## Notes

- Use the provided virtual environment `.venv` (added to `.gitignore`).
- Adjust `requirements.txt` when adding new dependencies.
