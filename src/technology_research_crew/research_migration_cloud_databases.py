from dotenv import load_dotenv
load_dotenv('env/.env')  # .env file is in the env folder with environment variables


import os
import sys
required_vars = ['SERPER_API_KEY', 'OPENAI_API_KEY']
for var in required_vars:
    if os.getenv(var) is None:
        print(f"Error: {var} is not set")
        sys.exit(1)

print("API keys are set")

from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
  role='Senior Researcher',
  goal='Uncover problems, solutions (methods, tools, and best practices), and opportunities in {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Driven by curiosity, you're at the forefront of database technologies innovation,"
    "eager to explore real customer problems, how they are soved today,"
    "identify gaps, and brainstorm new solutions that could move the industry to another level."
  ),

  tools=[search_tool],
  allow_delegation=True

)

# Creating a writer agent with custom tools and delegation capability
writer = Agent(
  role='Writer',
  goal='Narrate compelling and comprehensive reports about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging reports that are comprehensive and well structured,"
    "organizing concepts in taxonomies, in an accessible manner."
    "You prefer to write your reports in topics and subtopics."
  ),
  tools=[search_tool],
  allow_delegation=False
)

from crewai import Task

# Research task
research_task = Task(
  description=(
    "Identify the major existing services, tools, methods, and best practices,"
    "and the next big trends in {topic}."
    "Prefer technical documentation, tutorials, and engineering blog posts,"
    "user forums, knowlege bases, and scientific papers as the main source."
    "Focus on clearly stating the problem, identifying existing solutions,"
    "the pros and cons, exiting gaps, and potential new and better solutions."
    "Your final report should clearly articulate the problem, the solutions,"
    "the strenghts, and weaknesses, the opportunities, and the main risks to be addressed."
  ),

  expected_output='A comprehensive 10 paragraphs long technical report.',
  tools=[search_tool],
  agent=researcher,

)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful report on {topic}."
    "Focus on the existing problems, and solutions, as methods, services and tools,"
    "their gaps, and the potential opportunities based on the latest trends of the industry."
    "This article should be structure from major concepts to details, with topics and subtopics."
    "The conclusion should clearly list the opportunities to explore."
  ),

  expected_output='A 20 paragraph report on {topic} advancements formatted as markdown.',
  tools=[search_tool],
  agent=writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization

)

from crewai import Crew, Process

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)


# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'Cloud databases migration tools and services, with focus on MySQL as a target'})
print(result)