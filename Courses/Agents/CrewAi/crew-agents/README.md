# CrewAI Simple Agent

A simple CrewAI agent system that can answer questions using AI. This project demonstrates how to create and orchestrate autonomous AI agents using the CrewAI framework.

## Features

- 🤖 **Research Assistant Agent**: Knowledgeable agent that provides comprehensive answers
- 📝 **YAML Configuration**: Easy-to-modify agent and task configurations
- 🔑 **Environment Variables**: Secure API key management
- 💬 **Interactive CLI**: Simple command-line interface for asking questions

## Prerequisites

- Python 3.9+ (Python 3.10+ recommended)
- OpenAI API key
- pip or conda package manager

## Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd crew-agents
```

### 2. Install Dependencies

**Option A: Using pip (recommended)**
```bash
pip install crewai==0.1.32 python-dotenv pyyaml
```

**Option B: Using Poetry** (if you have poetry installed)
```bash
poetry install
```

### 3. Configure Environment

Copy the example environment file and add your OpenAI API key:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```bash
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
```

### 4. Run the Agent

```bash
python src/simple_agent/main.py
```

## Usage Examples

### Interactive Mode
```bash
python src/simple_agent/main.py
```
Then enter your question when prompted.

### Piped Input
```bash
echo "What are the benefits of artificial intelligence?" | python src/simple_agent/main.py
```

### Example Session
```
🤖 Simple Agent - Ask me anything!
----------------------------------------
What question would you like me to answer? What is the capital of France?

🔍 Processing your question: What is the capital of France?
----------------------------------------

✅ Answer:
----------------------------------------
The capital of France is Paris. It is not only the largest city in the country but also serves as a significant hub for business, culture, fashion, and gastronomy...
```

## Project Structure

```
crew-agents/
├── src/
│   └── simple_agent/
│       ├── __init__.py           # Package initialization
│       ├── main.py              # Main application entry point
│       └── config/
│           ├── agents.yaml      # Agent configurations
│           └── tasks.yaml       # Task definitions
├── .env                         # Environment variables (not in git)
├── .env.example                # Example environment file
├── .gitignore                  # Git ignore rules
├── pyproject.toml              # Project dependencies
└── README.md                   # This file
```

## Configuration

### Agents Configuration (`src/simple_agent/config/agents.yaml`)
```yaml
research_agent:
  role: Research Assistant
  goal: Provide accurate and helpful answers to user questions
  backstory: You are a knowledgeable research assistant...
```

### Tasks Configuration (`src/simple_agent/config/tasks.yaml`)
```yaml
answer_question:
  description: Answer the user's question: {question}
  expected_output: A clear, accurate, and helpful answer...
```

## Customization

### Adding New Agents

1. **Update `agents.yaml`**:
```yaml
new_agent:
  role: Specialist Role
  goal: Specific goal for this agent
  backstory: Background story for the agent
```

2. **Update `tasks.yaml`**:
```yaml
new_task:
  description: Task description with {variables}
  expected_output: Expected output format
```

3. **Modify `main.py`** to include the new agent and tasks.

### Changing LLM Models

Update the `.env` file to use different OpenAI models:
```bash
OPENAI_MODEL_NAME=gpt-4
OPENAI_API_BASE=https://api.openai.com/v1
```

## Troubleshooting

### Common Issues

**ModuleNotFoundError: No module named 'dotenv'**
```bash
pip install python-dotenv
```

**ModuleNotFoundError: No module named 'yaml'**
```bash
pip install pyyaml
```

**OpenAI API Key Error**
- Ensure your `.env` file contains a valid OpenAI API key
- Check that you have sufficient OpenAI API credits
- Verify the API key format starts with `sk-`

**Python Version Issues**
- CrewAI requires Python 3.9+
- Some features work better with Python 3.10+
- Use `python --version` to check your version

### Debugging

Enable verbose mode by setting the agent's `verbose=True` in the configuration to see detailed execution logs.

## Development

### Running Tests
```bash
python -c "import yaml, dotenv, crewai; print('All imports successful!')"
```

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add docstrings for functions and classes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python-dotenv Documentation](https://github.com/theskumar/python-dotenv)

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the CrewAI documentation
3. Open an issue in the repository

---

Built with ❤️ using [CrewAI](https://crewai.com/)