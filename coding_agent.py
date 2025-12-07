# coding_agent.py
"""
Coding Agent - AI-Powered Development Assistant
Copyright (c) 2025 Hasani Mkindi (AfroDemoz, ADz Community, kitaaTech)
GitHub: @afrodemo

An open-source coding agent that helps developers with various coding tasks using free AI APIs.
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import FileReadTool, FileWriterTool
from langchain_google_genai import ChatGoogleGenerativeAI

class CodingAgent:
    """Main coding agent class that provides file management and code generation capabilities."""

    def __init__(self, api_key=None):
        """Initialize the coding agent with API key."""
        # Load environment variables
        load_dotenv()

        # Set API key from environment or parameter
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in .env file.")
        os.environ["GOOGLE_API_KEY"] = self.api_key

        # Initialize LLM
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # A good, fast model for the free tier
            temperature=0.1  # Low temperature for more deterministic code output
        )

        # Create file manager agent
        self.file_manager = Agent(
            role='Senior File System Manager',
            goal='Accurately read, create, and modify project files based on user requests.',
            backstory='You are a meticulous software architect with perfect memory for file contents and structure.',
            verbose=True,
            allow_delegation=False,
            tools=[FileReadTool(), FileWriterTool()],
            llm=self.llm
        )

        print("✅ Coding Agent initialized successfully!")

    def execute_task(self, description, filename=None, expected_output=None):
        """Execute a coding task using the agent crew."""
        # Create task
        task = Task(
            description=description,
            expected_output=expected_output or "Task completed successfully",
            agent=self.file_manager
        )

        # Assemble crew and execute
        crew = Crew(
            agents=[self.file_manager],
            tasks=[task],
            process=Process.sequential
        )

        result = crew.kickoff()
        return result

    def read_file(self, filename):
        """Read the content of a file using the file manager agent."""
        # Create a simple read task
        read_task = Task(
            description=f"Read the content of file: {filename}",
            expected_output="The complete content of the requested file",
            agent=self.file_manager
        )

        crew = Crew(
            agents=[self.file_manager],
            tasks=[read_task],
            process=Process.sequential
        )

        return crew.kickoff()

    def create_file(self, filename, content):
        """Create a new file with the specified content."""
        # Create a file creation task
        create_task = Task(
            description=f"Create a new file named {filename} with the following content: {content}",
            expected_output="Confirmation that the file was created successfully",
            agent=self.file_manager
        )

        crew = Crew(
            agents=[self.file_manager],
            tasks=[create_task],
            process=Process.sequential
        )

        return crew.kickoff()

# Main execution (for backward compatibility)
if __name__ == "__main__":
    # --- 1. Load environment variables from .env file ---
    load_dotenv()

    # --- 2. Set your API Key from environment variables ---
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in .env file.")
    os.environ["GOOGLE_API_KEY"] = api_key

    # --- 2. Instantiate the LLM with Gemini ---
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # A good, fast model for the free tier
        temperature=0.1  # Low temperature for more deterministic code output
    )

    # --- 4. Create the File Manager Agent ---
    file_manager = Agent(
        role='Senior File System Manager',
        goal='Accurately read, create, and modify project files based on user requests.',
        backstory='You are a meticulous software architect with perfect memory for file contents and structure.',
        verbose=True,  # Set to True to see the agent's thought process
        allow_delegation=False,
        tools=[FileReadTool(), FileWriterTool()],  # Give the agent its tools
        llm=llm  # Connect it to the Gemini brain
    )

    print("✅ File Manager Agent created successfully!")

    # --- 5. Define a Task for the Agent ---
    code_task = Task(
        description="""1. First, read the file named 'main.py' if it exists.
        2. If it does NOT exist, create a new 'main.py' file.
        3. Write a simple Python function in it that calculates the factorial of a number.
        4. Ensure the code is clean and has a docstring.""",
        expected_output="A confirmation that the file has been created or updated with the correct code.",
        agent=file_manager
    )

    # --- 6. Assemble the Crew and Run the Task ---
    coding_crew = Crew(
        agents=[file_manager],
        tasks=[code_task],
        process=Process.sequential
    )

    # Execute the task!
    result = coding_crew.kickoff()
    print("\n--- Task Result ---")
    print(result)
