class Task:
    def __init__(self, name, deadline, duration, profit, priority):
        self.name = name
        self.deadline = int(deadline)
        self.duration = int(duration)
        self.profit = int(profit)
        self.priority = int(priority)

    def is_valid(self):
        return (
            self.deadline > 0 and
            self.duration > 0 and
            self.profit >= 0 and
            self.priority >= 0
        )

    def __repr__(self):
        return (
            f"Task(name={self.name}, "
            f"deadline={self.deadline}, "
            f"duration={self.duration}, "
            f"profit={self.profit}, "
            f"priority={self.priority})"
        )