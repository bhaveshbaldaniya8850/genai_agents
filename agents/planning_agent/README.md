# Planning Agent

The Planning Agent is designed to create a plan to achieve a given goal. It breaks down the goal into smaller, manageable steps.

## Capabilities

- **Goal Decomposition:** The agent can take a high-level goal and break it down into a series of smaller, actionable steps.
- **Plan Generation:** It provides a clear and concise plan that can be easily followed.

## Usage

To use the Planning Agent, you can import it into your Python code as follows:

```python
from agents.planning_agent.main import PlanningAgent

# Initialize the agent
planner = PlanningAgent()

# Use the agent
plan = planner.create_plan("Develop a new mobile application.")
