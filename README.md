# 🤖 Coding Agent - AI-Powered Development Assistant

An open-source coding agent that helps developers with various coding tasks using free AI APIs. This project leverages AI agents to assist with file management, code generation, and development tasks.

## 🚀 Features

- **AI-Powered File Management**: Automatically read, create, and modify project files
- **Code Generation**: Generate clean, well-documented code with proper structure
- **Multi-Agent System**: Uses CrewAI framework for coordinated task execution
- **Free AI APIs**: Designed to work with free-tier AI models like Gemini
- **Extensible Architecture**: Easy to add new tools and capabilities

## 📦 Installation

### Prerequisites
- Python 3.12+
- Virtual environment (recommended)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/coding-agent.git
   cd coding-agent
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Add your Google API key to the `.env` file:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🎯 Usage

### Basic Example

```python
from coding_agent import CodingAgent

# Initialize the agent
agent = CodingAgent(api_key="your_api_key")

# Create a new file with code
agent.create_file(
    filename="utils.py",
    content="""
def calculate_factorial(n):
    '''Calculate factorial of a number'''
    if n == 0:
        return 1
    return n * calculate_factorial(n-1)
"""
)

# Read an existing file
file_content = agent.read_file("main.py")
print(file_content)
```

### Advanced Usage

```python
from coding_agent import CodingCrew

# Create a team of agents
crew = CodingCrew(
    agents=[
        "file_manager",
        "code_reviewer",
        "test_writer"
    ]
)

# Execute complex tasks
result = crew.execute_task(
    description="Create a Flask API with user authentication",
    expected_output="A complete Flask application with auth routes"
)
```

## 🔧 Configuration

Create a `.env` file with your API keys:

```
GOOGLE_API_KEY=your_google_api_key
# Add other API keys as needed
```

## 📂 Project Structure

```
coding-agent/
├── coding_agent.py          # Main agent implementation
├── requirements.txt         # Python dependencies
├── README.md                 # Project documentation
├── .env.example              # Example environment file
└── examples/                 # Usage examples
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create your feature branch**: `git checkout -b feature/your-feature`
3. **Commit your changes**: `git commit -m 'Add some feature'`
4. **Push to the branch**: `git push origin feature/your-feature`
5. **Open a pull request**

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run linting
flake8 coding_agent.py
```

## 🌟 Supported AI APIs

- **Google Gemini** (Primary, free tier available)
- **OpenAI** (Optional, requires API key)
- **Anthropic Claude** (Optional)
- **Mistral** (Optional)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent framework
- [LangChain](https://github.com/langchain-ai/langchain) - LLM integration
- [Google Generative AI](https://ai.google.dev/) - Free AI API

## 👤 Project Founder & Credits

**Hasani Mkindi** - Founder & Creator
- **GitHub**: [@afrodemo](https://github.com/afrodemo)
- **From**: East Africa, Tanzania
- **Founder of**: AfroDemoz, ADz Community, and kitaaTech
- **Role**: Visionary behind the Coding Agent project

This project was created by Hasani Mkindi to empower developers in Africa and worldwide with AI-powered coding assistance using free APIs.

## 🤝 Special Thanks

Special thanks to the open-source community and all contributors who help make this project better!

## 🚀 Roadmap

- [ ] Add more coding tools (linters, formatters)
- [ ] Support for multiple programming languages
- [ ] Git integration for version control
- [ ] CI/CD pipeline automation
- [ ] Web interface for easier usage

---

**💡 Tip**: Start with simple tasks and gradually increase complexity as you become familiar with the agent's capabilities!

**🐛 Issues**: Found a bug? Please open an issue with detailed reproduction steps.

**⭐ Star**: If you find this project helpful, please star the repository!
