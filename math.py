import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from CalculateTool import calculate

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
## os.environ['OPENAI_MODEL_NAME'] = os.getenv('OPENAI_MODEL_NAME')

print("## Welcome to the math wizard ##")
math_input = input("Enter a math problem: ")

math_agent = Agent(
	role="Math Wizard",
	goal="you are able to calculate any math expresion",
	backstory="you are a math wizard",
    verbose=True,
    tools=[calculate]
)

writer = Agent(
    role="Writer",
    goal="Craft compelling explanations based from results of math equations.",
    backstory="You are a renowned Content Strategist, known for your insightful and engaging articles. You transform complex concepts into compelling narratives.",
    verbose=True
)

task1 = Task(
	description=f"{math_input}",
	expected_output="Give full details in bullets points.",
	agent=math_agent
)

task2 = Task(
	description="using the insight provided, explain in great detail how the opeations were done",
	expected_output="Explain in great detail and save in markdown. Do not add mark with triple tick marks at the end and the beginning of the file. Also don't say what type it is in the first line.",
	output_file="math_explanation.md",
    agent=writer
)

crew = Crew(
    agents=[math_agent, writer],
    tasks=[task1, task2],
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff()
print(result)
   