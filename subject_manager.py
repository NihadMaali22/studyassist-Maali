
import json

class SubjectManager:
    def load_subjects(self, filepath: str) -> list:
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                return data.get("subjects", [])
        except FileNotFoundError:
            raise FileNotFoundError(f"Subjects file not found: {filepath}")

    def get_subject(self, subjects: list, subject_id: str) -> dict:
        for subject in subjects:
            if subject.get("subject_id", "").upper() == subject_id.upper():
                return subject
        return None
 
    def get_weekly_goal(self, subjects: list, subject_id: str) -> int:
        subject = self.get_subject(subjects, subject_id)
        if not subject:
            raise ValueError("Subject not found")
        return subject.get("weekly_goal_hours", 0)

    def display_subjects(self, subjects: list) -> None:
        print(f"{'ID':<6} | {'Subject Name':<30} | {'Weekly Goal (hrs)':<17} | {'Instructor':<20}")
        print(f"{'-' * 6} | {'-' * 30} | {'-' * 17} | {'-' * 20}")
        for subject in subjects:
            subject_id = subject.get("subject_id", "")
            name = subject.get("name", "")
            weekly_goal = subject.get("weekly_goal_hours", 0)
            instructor = subject.get("instructor", "")
            print(f"{subject_id:<6} | {name:<30} | {weekly_goal:<17} | {instructor:<20}")
