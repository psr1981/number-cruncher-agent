from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import VisionTool
import os

@CrewBase
class NumberCruncherCrew:
    """Number Cruncher Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    #os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
    vision_tool = VisionTool()

    @agent
    def question_parser_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["question_parser_agent"],
        )

    @agent
    def answer_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["answer_generator_agent"],
        )
    
    @agent
    def prompt_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["prompt_generator_agent"],
        )

    #@agent
    #def image_text_extractor(self) -> Agent:
    #    return Agent(
    #        config=self.agents_config['image_text_extractor'],
    #       tools=[self.vision_tool],
    #        verbose=True
    #    )

    #@task
    #def extract_text_from_image(self) -> Task:
    #    return Task(
    #        config=self.tasks_config['extract_text_from_image'],
    #    )
    

    @task
    def parse_question(self) -> Task:
        return Task(
            config=self.tasks_config["parse_question"],
        )


    @task
    def generate_answer(self) -> Task:
        return Task(
            config=self.tasks_config["generate_answer"],
        )

    @task
    def generate_additional_prompts(self) -> Task:
        return Task(
            config=self.tasks_config["generate_additional_prompts"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Number Cruncher Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
