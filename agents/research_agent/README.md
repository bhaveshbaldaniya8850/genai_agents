# Research Agent

The Research Agent is designed to perform research on a given query. It simulates searching the web and returns a summary of its findings.

## Capabilities

- **Web Search Simulation:** The agent can take a query and simulate a web search to gather information.
- **Summarization:** It provides a concise summary of the information found.

## Usage

To use the Research Agent, you can import it into your Python code as follows:

```python
from agents.research_agent.main import ResearchAgent

# Initialize the agent
researcher = ResearchAgent()

# Use the agent
research_summary = researcher.search("What are the latest advancements in AI?")
