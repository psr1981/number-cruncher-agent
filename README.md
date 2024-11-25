# {{crew_name}} Crew

Welcome to the {{crew_name}} Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```


## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

**Add your `OPENAI_API_KEY` into the `.env` file**

```bash
crewai flow kickoff

```
This command initializes the Number Cruncher Crew, assembling the agents and assigning them tasks as defined in your configuration.


## Setup new question

```bash
vim question.txt
crewai flow kickoff

```
This command initializes the Number Cruncher Crew, assembling the agents and assigning them tasks as defined in your configuration.



## Support

For support, questions, or feedback regarding the {{crew_name}} Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)

