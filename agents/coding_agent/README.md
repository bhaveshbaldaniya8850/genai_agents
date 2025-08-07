# Coding Agent

The Coding Agent is designed to generate code based on a given prompt. It can be used to automate coding tasks and generate boilerplate code.

## Capabilities

- **Code Generation:** The agent can take a prompt and generate a code snippet.
- **Boilerplate Code:** It can be used to generate repetitive code structures.

## Usage

To use the Coding Agent, you can import it into your Python code as follows:

```python
from agents.coding_agent.main import CodingAgent

# Initialize the agent
coder = CodingAgent()

# Use the agent
code_snippet = coder.generate_code("Create a Python function to calculate the factorial of a number.")
