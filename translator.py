from src.text.single_prompt import SinglePromptAgent
from src.utils.colored_print import colored_print

def translator_function(text: str) -> None:
    print("Text to translate:", text)
    # Write a template with the variable you will use
    template = '''
    Translate this text

    {text_to_translate} 

    into Ukrainian
    '''

    # Instanciate the SinglePromptAgent with the right template 
    agent = SinglePromptAgent(template=template)

    # Run the agent with the variable needed to the prompt execution
    colored_print(agent.run(text_to_translate=text), 'blue')


if __name__ == '__main__':
        import sys
        if len(sys.argv) > 1:
                text_to_translate = sys.argv[1]
                translator_function(text_to_translate)
        else:
                print("No text to translate provided.")
