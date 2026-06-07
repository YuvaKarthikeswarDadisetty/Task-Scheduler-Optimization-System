def generate_timeline(tasks):
    timeline = []
    current_time = 0

    print("\n⏱️ Execution Timeline:")
    print("-" * 60)

    for task in tasks:
        start = current_time
        end = current_time + task.duration

        timeline.append((task.name, start, end))
        current_time = end

        print(f"{task.name}: Start={start}, End={end}")

    print("-" * 60)

    return timeline


def calculate_performance(all_tasks, scheduled_tasks):
    scheduled_names = set(task.name for task in scheduled_tasks)

    total_profit = sum(task.profit for task in scheduled_tasks)

    missed_tasks = [
        task for task in all_tasks if task.name not in scheduled_names
    ]

    print("\n📈 Performance Summary:")
    print("-" * 60)
    print(f"💰 Total Profit: {total_profit}")
    print(f"✅ Completed Tasks: {len(scheduled_tasks)}")
    print(f"❌ Missed Tasks: {len(missed_tasks)}")
    print("-" * 60)

    return total_profit, missed_tasks


def display_missed_tasks(missed_tasks):
    print("\n❌ Missed Tasks:")
    print("-" * 60)

    for task in missed_tasks:
        print(task)

    print("-" * 60)