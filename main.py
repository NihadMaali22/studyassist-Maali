from pathlib import Path

from subject_manager import SubjectManager
from session_manager import SessionManager
from visualizer import Visualizer

def main():
    data_root = Path(__file__).resolve().parent.parent
    SUBJECTS_FILE = str(data_root / "subjects.json")
    LOG_FILE = str(data_root / "session_log.csv")

    sm  = SubjectManager()
    ssm = SessionManager()
    viz = Visualizer()

    # Step 1: Load data
    print("[1/5] Loading data...")
    subjects = sm.load_subjects(SUBJECTS_FILE)
    log      = ssm.load_log(LOG_FILE)
    print(f"      Subjects loaded : {len(subjects)}")
    print(f"      Sessions loaded : {len(log)}\n")

    # Step 2: Display subjects
    print("[2/5] Registered subjects:")
    sm.display_subjects(subjects)

    # Step 3: Display sessions for a subject
    print("\n[3/5] Sessions for CS301 (Artificial Intelligence):")
    cs301_sessions = ssm.get_by_subject(log, "CS301")
    for s in cs301_sessions:
        print(f"      {s['date']}  |  {s['topic']:<25}  |  {s['duration_min']} min")

    # Step 4: Log a new test session
    print("\n[4/5] Logging a new study session...")
    try:
        log = ssm.add_session(log, subject_id="CS101", duration_min=45,
                              topic="Matplotlib basics", notes="Practice charts")
        ssm.save_log(log, LOG_FILE)
    except ValueError as e:
        print(f"      Failed: {e}")

    # Step 5: Visualize
    print("\n[5/5] Displaying charts...")
    hours = ssm.analyze_hours(log)
    viz.hours_bar_chart(hours)
    viz.goal_pie_chart(hours, subjects)

    print("\nDone!")

if __name__ == "__main__":
    main()