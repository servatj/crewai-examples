import os
from dotenv import load_dotenv
# from tools.browser_tools import BrowserTools
# from tools.search_tools import SearchTools

load_dotenv()

from crewai import Agent, Task, Crew, Process
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

mistral_api_key = os.getenv("MISTRAL_API_KEY")
llm_mistral = ChatMistralAI(api_key=mistral_api_key, model="mistral-medium")

influencer = Agent(
    role="Influencer", 
    goal="Write a catchy, emoji-filled tweet about good healthy habits.",
    backstory="I'm a social media influencer with a large following. I need to write 2 tweet that will get a lot of engagement.",
    verbose=True,
    allow_delegation=False
)

feedback = Agent(
    role="Feedback", 
	goal="Provide feedback on a new linkedin posts.",
	backstory="I'm a influencer who needs feedback on likedin posts.",
	verbose=True,
	allow_delegation=False
)

email = Agent(
	role="Email", 
	goal="Write an email to a potential client.",
	backstory="I'm a salesperson who needs to write an email to a potential client.",
	verbose=True,
	allow_delegation=True
)

coach = Agent(
    role='coach',
    goal="Discover and examine key tech and AI career skills for 2024",
    backstory="You're an expert in spotting new trends and essential skills in AI and technology.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
)

task_search = Task(
    description="Search for information about the latest iPhone release.",
    expected_output="A summary of the latest iPhone release.",
    agent=coach
)

task_post = Task(
    description="Create a linkedin post",
    expected_output="A catchy, emoji-filled tweet about healthy habits",	
    agent=influencer
)

task_feedback = Task(
    description="Provide feedback on the new post",
	expected_output="Feedback on the new post, if it can be improved make new suggestions.",
	agent=feedback
)

team = Crew(
    agents=[influencer, feedback],
    tasks=[task_post, task_feedback],
    verbose=True,
    process=Process.sequential
)

result = team.kickoff()
# print(result)
   
