from src.cli import TaskSchedulerCLI


def main():
    print("🚀 Task Scheduler Optimization System (CLI Mode)")
    app = TaskSchedulerCLI()
    app.menu()


if __name__ == "__main__":
    main()