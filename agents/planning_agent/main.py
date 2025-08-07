class PlanningAgent:
    def create_plan(self, goal: str) -> list[str]:
        """
        Simulates creating a plan and returns a pre-defined list of steps.
        """
        return [f"Step 1: Define the goal - {goal}", "Step 2: Break down the goal into smaller tasks.", "Step 3: Execute the tasks."]
