from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class NumberCruncherCrew:
    """Number Cruncher Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

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

    @crew
    def crew(self) -> Crew:
        """Creates the Number Cruncher Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
