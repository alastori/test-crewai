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
  goal='Uncover methods, tools, and best practices in {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Driven by curiosity, you're at the forefront of"
    "innovation, eager to explore and share knowledge that could move"
    "the industry to another level."
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
    "organizing concepts in taxonomies, bringing trends and existing,"
    "technologies to light in an accessible manner."
  ),
  tools=[search_tool],
  allow_delegation=False
)

from crewai import Task

# Research task
research_task = Task(
  description=(
    "Identify the major existing methods, tools, and best practices,"
    "and the next big trends in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "strenghts, and weaknesses, market opportunities, and potential risks."
  ),

  expected_output='A comprehensive 5 paragraphs long technical report.',
  tools=[search_tool],
  agent=researcher,

)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful report on {topic}."
    "Focus on the existing methods and tools, and the latest trends,"
    "and how it's impacting the users and the industry."
    "This article should be structure from major concepts to detais,"
    "and easy to understand."
  ),

  expected_output='A 10 paragraph report on {topic} advancements formatted as markdown.',
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
result = crew.kickoff(inputs={'topic': 'Cloud databases migration tools and services compatible with MySQL'})
print(result)