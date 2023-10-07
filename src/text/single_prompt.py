
import argparse

from langchain.chat_models import ChatOpenAI

from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate
)
import os
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
load_dotenv()


class SinglePromptAgent:
    def __init__(self,
                temperature: int = 0.5, 
                openai_api_key: str = '',
                template: str = 
                '''
                Your are an useful assistant

                User message: {user_message}
                ''',
                model: str= 'gpt-3.5-turbo'):
        self.system_template = template
        # self.human_template = '{letter_to_format}'
        # The temperature parameter controls the randomness of the model's output
        # with a lower temperature resulting in more deterministic output.
        api_key = openai_api_key or os.environ.get("OPENAI_API_KEY")
        self.chat = ChatOpenAI(temperature=temperature, 
                               model=model, 
                               openai_api_key=api_key)


        # You can use the SystemMessagePromptTemplate.from_template to transform a single text
        # into a prompt with variables
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)


        # self.user_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template)



        # Combine the system and human prompts into a single chat prompt.
        # Availiable schemas are:
        # SystemMessagePromptTemplate,
        # HumanMessagePromptTemplate,
        # AIMessagePromptTemplate

        self.chat_prompt = ChatPromptTemplate.from_messages(
            # [self.system_message_prompt, self.user_message_prompt]
            [self.system_message_prompt]
        )

        
        # Create an instance of LLMChain
        self.chain = LLMChain(llm=self.chat, prompt=self.chat_prompt)

    def run(self,callback=None,**args):
        agent_response = self.chain.run(
            **args
        )
        if callback:
            return callback(agent_response)
        return agent_response


def main():
    agent = SinglePromptAgent()

    structure= '''
    Title ``Title of the post``

    Description ``Description of the post``

    #tags #another_tag ``Include here the tags``
    '''

    context="""
    The organization is called 4Geeks Academy.
The organization's mission is “Empowering talent with code by providing flexible educational experiences”. We want to be the most relevant career-boosting community for future and present coders.
We offer bootcamps in coding-related careers like Full Stack Development Bootcamp, Software Engineering Bootcamp, DataScience Bootcamp, Web3, and Blockchain Bootcamp.
Mainly, we target people from 25 to 38 years old that are not currently satisfied with their current job and careers and what to make a switch to tech. Secondly, we also target young people from 18 to 24 years old looking to start a career in tech, they may skip or postpone university studies to join the bootcamp.
When you enroll, we onboard you with a 4 months intensive course to get momentum, and you get access to lifetime career support with unlimited 1-1 mentorships, live workshops, and events every week, live master classes with experts 3 times a week, resume building preparation, mock interview preparation, access to our online platform with thousands of exercises with interactive grading, solutions, and videos.
Usually, new clients are concerned about the course price, how long they take, how much help they will receive to get a job, and the minimum experience or knowledge requirements to join the courses.
The big majority of your students receive total or partial scholarships. We have a 20 million dollar fund that offers several ways to benefit: You can apply for an entire ride, income share agreement, very flexible payment plans, and many other ways. We also offer a "job guaranty" option where if you decide to pay for the course and you don't get a job 90 days after graduation, we will give you back your money.
    """
    print(agent.run(
        objective="You need to provide an useful Twitter post based in a description, make sure of include proper tags to make the post more engaging to the users",
        response_structure=structure,
        context=context
    ))


if __name__ == '__main__':
    main()