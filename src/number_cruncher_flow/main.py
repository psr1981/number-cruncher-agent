#!/usr/bin/env python
from random import randint

from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

from .crews.number_cruncher_crew.number_cruncher_crew import NumberCruncherCrew

#question_text = "header [id   name ] \n Row no 1 [ 1001  tom ] \n Row no 2 [ 1002  jerry ]  \n Row no 3 [ 1003  harry ]  \n   What is the id for aaa ?"
#question_text = "what is the capital of france ?"
question_text = "In a triagle, side a is 60 degree, side b is 60 degree then what will be value of side c ?"


class NumberCruncherState(BaseModel):
    question_text: str = " "
    question_response: str = ""


class NumberCruncherFlow(Flow[NumberCruncherState]):

    @start()
    def load_question_text(self):
        print("Loading question text")
        self.state.question_text = question_text
        print (self.state.question_text)

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
