# StudyAssist Project Report

GitHub URL: https://github.com/NihadMaali22/studyassist-Maali

## Overview
StudyAssist is a small Python project for tracking and visualizing study sessions by subject. It loads subject definitions from a JSON file, reads session logs from CSV, prints summaries to the console, adds a sample session, and displays simple charts.

## Key Features
- Load subjects from `subjects.json` and sessions from `session_log.csv`.
- Display registered subjects in a formatted table.
- Filter sessions by subject and list them in the console.
- Add a new study session with validation and save back to CSV.
- Visualize total hours per subject (bar chart) and distribution (pie chart).

## Main Components
- `main.py` orchestrates the workflow: load data, show subjects and sessions, append a new entry, and render charts.
- `subject_manager.py` handles loading subjects and formatting subject listings.
- `session_manager.py` loads/saves session logs, validates new sessions, and aggregates study time.
- `visualizer.py` renders charts using Matplotlib.
- `create_sample_data.py` generates sample JSON and CSV data.

## Data Files
- `subjects.json` stores subject metadata (id, name, weekly goal, instructor).
- `session_log.csv` stores session logs (id, subject, date, duration, topic, notes).

## How To Run
1. Activate the virtual environment and install dependencies from `requirements.txt`.
2. Run the app:
   - `python studyassist-Maali/main.py`

## Notes
- Matplotlib is required for charts.
- The script appends a new session each run, then saves the updated log.
