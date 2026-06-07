import csv
import os


OUTPUT_DIR = "outputs"


def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def save_timeline(timeline):
    ensure_output_dir()
    file_path = os.path.join(OUTPUT_DIR, "timeline.csv")

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Task", "Start Time", "End Time"])

        for task_name, start, end in timeline:
            writer.writerow([task_name, start, end])

    print(f"📁 Timeline saved to {file_path}")


def save_missed_tasks(missed_tasks):
    ensure_output_dir()
    file_path = os.path.join(OUTPUT_DIR, "missed_tasks.csv")

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Task", "Deadline", "Duration", "Profit", "Priority"])

        for task in missed_tasks:
            writer.writerow([
                task.name,
                task.deadline,
                task.duration,
                task.profit,
                task.priority
            ])

    print(f"📁 Missed tasks saved to {file_path}")


def save_summary(total_profit, completed_count, missed_count):
    ensure_output_dir()
    file_path = os.path.join(OUTPUT_DIR, "summary.txt")

    with open(file_path, mode="w") as file:
        file.write("TASK SCHEDULER PERFORMANCE REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Total Profit: {total_profit}\n")
        file.write(f"Completed Tasks: {completed_count}\n")
        file.write(f"Missed Tasks: {missed_count}\n")

    print(f"📁 Summary saved to {file_path}")