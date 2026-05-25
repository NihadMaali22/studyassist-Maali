import matplotlib.pyplot as plt  # type:ignore[reportMissingModuleSource]


class Visualizer:
    def hours_bar_chart(self, hours_per_subject: dict):
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(
            hours_per_subject.keys(),
            hours_per_subject.values(),
            color="steelblue",
            edgecolor="white",
        )
        ax.set_title("Total Study Hours per Subject")
        ax.set_xlabel("Subject")
        ax.set_ylabel("Hours")
        plt.tight_layout()
        plt.show()

    def goal_pie_chart(self, hours_per_subject: dict, subjects: list):
        labels = []
        for sid, hrs in hours_per_subject.items():
            name = next((s["name"] for s in subjects if s["subject_id"] == sid), sid)
            labels.append(f"{name}\n({hrs}h)")

        fig, ax = plt.subplots(figsize=(7, 7))
        ax.pie(
            hours_per_subject.values(),
            labels=labels,
            autopct="%1.1f%%",
            startangle=140,
        )
        ax.set_title("Study Time Distribution by Subject")
        plt.tight_layout()
        plt.show()
        
        