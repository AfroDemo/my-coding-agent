#!/usr/bin/env python3
"""
Simple Example: Using the Coding Agent to create a basic Python function
"""

from coding_agent import CodingAgent

def main():
    # Initialize the coding agent
    agent = CodingAgent()

    # Example 1: Create a simple utility function
    print("🚀 Creating a simple utility function...")

    result = agent.execute_task(
        description="Create a Python function that calculates the factorial of a number",
        filename="utils/factorial.py",
        expected_output="A clean Python function with proper docstring"
    )

    print(f"✅ Task completed: {result}")

    # Example 2: Read the created file
    print("\n📖 Reading the created file...")

    file_content = agent.read_file("utils/factorial.py")
    print("File content:")
    print(file_content)

    # Example 3: Create a test file
    print("\n🧪 Creating a test file...")

    test_result = agent.execute_task(
        description="Create a test function for the factorial function using pytest",
        filename="tests/test_factorial.py",
        expected_output="A pytest test case for the factorial function"
    )

    print(f"✅ Test file created: {test_result}")

if __name__ == "__main__":
    main()
