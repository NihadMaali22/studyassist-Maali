import csv
from datetime import datetime

class SessionManager:
    def __init__(self, filepath: str | None = None):
        self.filepath = filepath

    def load_sessions(self, filepath: str | None = None) -> list:
        if filepath is None:
            filepath = self.filepath
        if not filepath:
            raise ValueError("Session log filepath is required")
        sessions = []
        try:
            with open(filepath, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["duration_min"] = int(row["duration_min"])
                    sessions.append(row)
        except FileNotFoundError:
            return []

        return sessions

    def load_log(self, filepath: str) -> list:
        return self.load_sessions(filepath)

    def save_log(self, log: list, filepath: str) -> None:
        fieldnames = ["session_id", "subject_id", "date", "duration_min", "topic", "notes"]
        with open(filepath, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in log:
                if "duration_min" in row:
                    try:
                        row["duration_min"] = int(row["duration_min"])
                    except (ValueError, TypeError):
                        pass
                writer.writerow(row)

        print(f"Saved {len(log)} sessions to {filepath}")

    def add_session(self, log: list, subject_id: str, duration_min: int, topic: str, notes: str = "") -> list:
        if duration_min <= 0:
            raise ValueError("Duration must be greater than 0 minutes")

        if not topic.strip():
            raise ValueError("Topic cannot be empty")

        new_id = f"S{len(log) + 1:03d}"
        date = datetime.now().strftime("%Y-%m-%d")
        session = {
            "session_id": new_id,
            "subject_id": subject_id,
            "date": date,
            "duration_min": duration_min,
            "topic": topic,
            "notes": notes,
        }
        log.append(session)
        print(f"Session logged: {new_id}-{topic} ({duration_min} min) for {subject_id}")
        return log
    
    def get_by_subject(self, log: list, subject_id: str) -> list:
        return [s for s in log if s["subject_id"] == subject_id]
    
    def analyze_hours(self, log: list) -> dict:
        hours = {}
        for s in log:
            hours[s["subject_id"]] = hours.get(s["subject_id"], 0) + s["duration_min"]
        return {k: round(v / 60, 2) for k, v in hours.items()}
