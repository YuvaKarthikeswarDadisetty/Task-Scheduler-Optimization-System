from ortools.sat.python import cp_model


def solve_with_cp_sat(tasks):
    model = cp_model.CpModel()

    n = len(tasks)

    # Decision variables
    x = [model.NewBoolVar(f"x_{i}") for i in range(n)]

    # Objective: maximize profit
    model.Maximize(
        sum(tasks[i].profit * x[i] for i in range(n))
    )

    # Constraint: cumulative scheduling (simplified)
    # Ensure total duration does not exceed max deadline
    max_deadline = max(task.deadline for task in tasks)

    model.Add(
        sum(tasks[i].duration * x[i] for i in range(n)) <= max_deadline
    )

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    selected_tasks = []

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("\n🧠 CP-SAT Optimal Solution:")
        print("-" * 60)

        for i in range(n):
            if solver.Value(x[i]) == 1:
                selected_tasks.append(tasks[i])
                print(tasks[i])

        print("-" * 60)
        print(f"💰 Optimal Profit: {solver.ObjectiveValue()}")

    else:
        print("❌ No feasible solution found.")

    return selected_tasks