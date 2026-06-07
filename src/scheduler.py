import heapq


def sort_tasks(tasks):
    return sorted(tasks, key=lambda t: (t.deadline, -t.priority, -t.profit))


def display_sorted_tasks(tasks):
    print("\n📊 Sorted Tasks (Deadline → Priority → Profit):")
    print("-" * 60)
    for task in tasks:
        print(task)
    print("-" * 60)


def greedy_schedule(tasks):
    min_heap = []
    current_time = 0

    for task in tasks:
        heapq.heappush(min_heap, (task.profit, task))
        current_time += task.duration

        print(f"\n➡️ Considering: {task.name}")
        print(f"   Current Time: {current_time}")

        if current_time > task.deadline:
            removed = heapq.heappop(min_heap)
            current_time -= removed[1].duration

            print(f"   ❌ Removed (Low Profit): {removed[1].name}")
            print(f"   Adjusted Time: {current_time}")

    return [item[1] for item in min_heap]


def display_final_schedule(tasks):
    print("\n✅ Final Optimized Schedule:")
    print("-" * 60)
    for task in tasks:
        print(task)
    print("-" * 60)