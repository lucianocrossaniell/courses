#!/usr/bin/env python3

import sys
import os
import yaml
from pathlib import Path
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# Load environment variables from .env file
load_dotenv()


class SimpleAgentCrew():
    """Simple Agent Crew"""
    
    def __init__(self):
        # Load config files
        config_dir = Path(__file__).parent / 'config'
        with open(config_dir / 'agents.yaml', 'r') as f:
            self.agents_config = yaml.safe_load(f)
        with open(config_dir / 'tasks.yaml', 'r') as f:
            self.tasks_config = yaml.safe_load(f)

    def research_agent(self) -> Agent:
        config = self.agents_config['research_agent']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=True
        )

    def answer_question_task(self, question: str) -> Task:
        config = self.tasks_config['answer_question']
        return Task(
            description=config['description'].format(question=question),
            expected_output=config['expected_output'],
            agent=self.research_agent()
        )

    def crew(self, question: str) -> Crew:
        """Creates the Simple Agent crew"""
        return Crew(
            agents=[self.research_agent()],
            tasks=[self.answer_question_task(question)],
            process=Process.sequential,
            verbose=True,
        )


def run():
    """
    Run the crew.
    """
    print("🤖 Simple Agent - Ask me anything!")
    print("-" * 40)
    
    question = input("What question would you like me to answer? ")
    
    if not question.strip():
        print("Please provide a question!")
        return
    
    print(f"\n🔍 Processing your question: {question}")
    print("-" * 40)
    
    inputs = {'question': question}
    
    # Check if API key is set
    if not os.getenv('OPENAI_API_KEY'):
        print("\n❌ Error: OPENAI_API_KEY not found!")
        print("Please set your OpenAI API key in the .env file.")
        return
    
    try:
        crew_instance = SimpleAgentCrew()
        result = crew_instance.crew(question).kickoff()
        print("\n✅ Answer:")
        print("-" * 40)
        print(result)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Make sure your OPENAI_API_KEY is valid and you have sufficient credits.")


if __name__ == "__main__":
    run()