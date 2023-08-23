import random
from src.text.single_prompt import SinglePromptAgent
from src.utils.colored_print import colored_print
from src.utils.create_file import create_file
from langchain.callbacks import get_openai_callback


def chat_interface():
        
        explanation = '''
        This script is a sample of how easy is to build a chat interface with the
        SinglePromptAgent of the source directory

        Send get_summary() to get the current conversation summary

        Start a conversation adding your name
        
        '''
        print(explanation)

        name = input("What is your name? \n")
        summary = 'Summary\n'

        while True:
            with get_openai_callback() as callback:
                last_messages = ''
                user_message = input("Your message: ")
                if user_message == 'get_summary()':
                    print(summary)
                    continue
                
                colored_print(user_message, 'blue')
                last_messages += (f'{name}: {user_message}')
                bot_message = generate_ai_answer(user_message, summary)
                last_messages += f'Assistant: {bot_message}'
                colored_print(bot_message)

                if 'export_txt()' in user_message:
                    create_file(filename=generate_random_phrase() + '.txt', content=bot_message)
                summary += summarize_conversation(summary=summary, last_messages=last_messages)
                    
                print(callback.total_cost)
                print(callback.total_tokens)
        

def generate_ai_answer(message:str, summary:str):
    _template = '''
    Your are a helpful assistant, answer the user message as best as you can

    This is the conversation summary:
    {summary}

    This is the user message:
    {message}

    '''
    agent = SinglePromptAgent(template=_template)

    
    return agent.run(message=message, summary=summary)



def generate_random_phrase():
    words = ["apple", "banana", "cat", "dog", "elephant", "fish", "gorilla", "horse", "iguana", "jaguar", "koala", "lion", "monkey", "newt", "octopus", "penguin", "quokka", "rabbit", "sheep", "tiger", "unicorn", "vulture", "whale", "zebra"]
    return '_'.join(random.sample(words, 3))

def summarize_conversation(summary:str, last_messages:str):
    template = '''
    Update the summary of this conversation:

    Current summary: {summary}

    Last messages: {last_messages}

    Give the new summary using as less words as you can
    '''
    agent = SinglePromptAgent(template=template)
    return agent.run(summary=summary, last_messages=last_messages)

if __name__ == "__main__":
        chat_interface()