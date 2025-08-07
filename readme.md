# Autonomous AI Agents

This project provides a set of three autonomous AI agents that can be easily integrated into your AI systems or chatbots. The agents are designed to be powerful, productive, and versatile, each with a specific function.

## Agents

This project includes the following agents:

### 1. Research Agent

The Research Agent is designed to perform research on a given query. It simulates searching the web and returns a summary of its findings.

For more information, see the [Research Agent README](./agents/research_agent/README.md).

### 2. Coding Agent

The Coding Agent is designed to generate code based on a given prompt. It can be used to automate coding tasks and generate boilerplate code.

For more information, see the [Coding Agent README](./agents/coding_agent/README.md).

### 3. Planning Agent

The Planning Agent is designed to create a plan to achieve a given goal. It breaks down the goal into smaller, manageable steps.

For more information, see the [Planning Agent README](./agents/planning_agent/README.md).

## Integration

To use these agents, you can import them into your Python code as follows:

```python
from agents.research_agent.main import ResearchAgent
from agents.coding_agent.main import CodingAgent
from agents.planning_agent.main import PlanningAgent

# Initialize the agents
researcher = ResearchAgent()
coder = CodingAgent()
planner = PlanningAgent()

# Use the agents
research_summary = researcher.search("What are the latest advancements in AI?")
code_snippet = coder.generate_code("Create a Python function to calculate the factorial of a number.")
plan = planner.create_plan("Develop a new mobile application.")

print("Research Summary:", research_summary)
print("Generated Code:", code_snippet)
print("Plan:", plan)
```
