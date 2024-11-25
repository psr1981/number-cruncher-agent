#!/usr/bin/env python
from random import randint

from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from .crews.number_cruncher_crew.number_cruncher_crew import NumberCruncherCrew
from .question_tools import read_question

# read question
question_text=read_question('question.txt')

#image_url = "https://m.media-amazon.com/images/M/MV5BNDUwNjBkMmUtZjM2My00NmM4LTlmOWQtNWE5YTdmN2Y2MTgxXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg"
#image_url = "https://d13ot9o61jdzpp.cloudfront.net/images/tabular_data_1_ideal_layout.png"
image_url = ""

class NumberCruncherState(BaseModel):
    question_text: str = ""
    image_url: str = ""
    question_response: str = ""


class NumberCruncherFlow(Flow[NumberCruncherState]):

    @start()
    def load_question_text(self):
        print("Loading question text")
        self.state.question_text = question_text
        self.state.image_url = image_url

    @listen(load_question_text)
    def generate_question_response(self):
        print("Generating question response")
        result = (
            NumberCruncherCrew()
            .crew()
            .kickoff(
                inputs={
                    "question_text": self.state.question_text,
                }
            )
        )

        print("Response generated", result.raw)
        self.state.question_response = result.raw

    @listen(generate_question_response)
    def save_question_response(self):
        print("printing question response")
        print(self.state.question_response)

def kickoff():
    number_cruncher_flow = NumberCruncherFlow()
    number_cruncher_flow.kickoff()


def plot():
    number_cruncher_flow = NumberCruncherFlow()
    number_cruncher_flow.plot()


if __name__ == "__main__":
    kickoff()
