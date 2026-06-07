from src.input_handler import load_tasks_from_csv
from src.scheduler import (
    sort_tasks,
    greedy_schedule,
    display_sorted_tasks,
    display_final_schedule
)
from src.analyzer import (
    generate_timeline,
    calculate_performance,
    display_missed_tasks
)
from src.reporter import (
    save_timeline,
    save_missed_tasks,
    save_summary
)
from src.cp_sat_solver import solve_with_cp_sat


class TaskSchedulerCLI:
    def __init__(self):
        self.tasks = []
        self.sorted_tasks = []
        self.scheduled_tasks = []
        self.timeline = []
        self.total_profit = 0
        self.missed_tasks = []
        self.optimal_tasks = []

    def menu(self):
        while True:
            print("\n===== TASK SCHEDULER MENU =====")
            print("1. Load Tasks from CSV")
            print("2. View Loaded Tasks")
            print("3. Sort Tasks")
            print("4. Run Greedy Scheduler")
            print("5. Run Optimal Solver (CP-SAT)")
            print("6. View Results")
            print("7. Export Reports")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.load_tasks()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.sort_tasks()
            elif choice == "4":
                self.run_scheduler()
            elif choice == "5":
                self.run_cp_sat()
            elif choice == "6":
                self.view_results()
            elif choice == "7":
                self.export_reports()
            elif choice == "8":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice. Try again.")

    def load_tasks(self):
        path = input("Enter CSV file path (default: data/tasks.csv): ").strip()
        if not path:
            path = "data/tasks.csv"

        self.tasks = load_tasks_from_csv(path)

        if self.tasks:
            print(f"✅ Loaded {len(self.tasks)} tasks successfully!")
        else:
            print("❌ No tasks loaded.")

    def view_tasks(self):
        if not self.tasks:
            print("⚠️ No tasks loaded.")
            return

        print("\n📋 Tasks:")
        for t in self.tasks:
            print(t)

    def sort_tasks(self):
        if not self.tasks:
            print("⚠️ Load tasks first.")
            return

        self.sorted_tasks = sort_tasks(self.tasks)
        display_sorted_tasks(self.sorted_tasks)

    def run_scheduler(self):
        if not self.sorted_tasks:
            print("⚠️ Sort tasks first.")
            return

        self.scheduled_tasks = greedy_schedule(self.sorted_tasks)
        display_final_schedule(self.scheduled_tasks)

        self.timeline = generate_timeline(self.scheduled_tasks)
        self.total_profit, self.missed_tasks = calculate_performance(
            self.tasks, self.scheduled_tasks
        )

    def run_cp_sat(self):
        if not self.tasks:
            print("⚠️ Load tasks first.")
            return

        self.optimal_tasks = solve_with_cp_sat(self.tasks)

    def view_results(self):
        print("\n📊 RESULTS COMPARISON")

        if self.scheduled_tasks:
            print("\n⚡ Greedy Solution:")
            display_final_schedule(self.scheduled_tasks)
            print(f"💰 Profit: {self.total_profit}")

        if self.optimal_tasks:
            print("\n🧠 Optimal CP-SAT Solution:")
            for t in self.optimal_tasks:
                print(t)

    def export_reports(self):
        if not self.timeline:
            print("⚠️ Run scheduler first.")
            return

        save_timeline(self.timeline)
        save_missed_tasks(self.missed_tasks)
        save_summary(
            self.total_profit,
            len(self.scheduled_tasks),
            len(self.missed_tasks)
        )

        print("✅ Reports exported successfully!")