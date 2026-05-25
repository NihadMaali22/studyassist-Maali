import json
import csv

def create_subjects(filepath="subjects.json"):
    data = {
        "subjects": [
            {"subject_id": "CS101", "name": "Python Programming",    "weekly_goal_hours": 5, "instructor": "Dr. Ahmad"},
            {"subject_id": "CS201", "name": "Data Structures",       "weekly_goal_hours": 4, "instructor": "Dr. Sara"},
            {"subject_id": "CS301", "name": "Artificial Intelligence","weekly_goal_hours": 6, "instructor": "Dr. Khalid"},
            {"subject_id": "CS401", "name": "Computer Networks",     "weekly_goal_hours": 3, "instructor": "Dr. Hani"},
        ]
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Subjects saved: {filepath}")

def create_session_log(filepath="session_log.csv"):
    rows = [
        ["session_id", "subject_id", "date",       "duration_min", "topic",                  "notes"],
        ["S001",       "CS101",      "2026-05-10",  "90",           "Loops and functions",    "Completed chapter 3"],
        ["S002",       "CS201",      "2026-05-10",  "60",           "Binary trees",           "Read slides + exercises"],
        ["S003",       "CS301",      "2026-05-11",  "120",          "Neural networks",        "Watched lecture video"],
        ["S004",       "CS101",      "2026-05-11",  "75",           "OOP basics",             "Wrote sample classes"],
        ["S005",       "CS401",      "2026-05-12",  "50",           "OSI model",              "Reviewed layers 1-4"],
        ["S006",       "CS301",      "2026-05-12",  "100",          "Decision trees",         "Implemented ID3 algorithm"],
        ["S007",       "CS201",      "2026-05-13",  "80",           "Graph traversal",        "BFS and DFS practice"],
        ["S008",       "CS101",      "2026-05-13",  "60",           "File handling",          "CSV and JSON practice"],
        ["S009",       "CS301",      "2026-05-14",  "90",           "K-means clustering",     "Dataset experiments"],
        ["S010",       "CS401",      "2026-05-14",  "45",           "TCP/IP",                 "Quiz preparation"],
    ]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Session log saved: {filepath}")

if __name__ == "__main__":
    create_subjects()
    create_session_log()