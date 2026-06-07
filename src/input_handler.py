import csv
from src.task import Task


def load_tasks_from_csv(file_path):
    tasks = []

    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    task = Task(
                        name=row['name'],
                        deadline=row['deadline'],
                        duration=row['duration'],
                        profit=row['profit'],
                        priority=row['priority']
                    )

                    if task.is_valid():
                        tasks.append(task)
                    else:
                        print(f"⚠️ Invalid Task Skipped: {row}")

                except Exception as e:
                    print(f"⚠️ Error parsing row {row}: {e}")

    except FileNotFoundError:
        print("❌ CSV file not found!")
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")

    return tasks