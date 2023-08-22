
from src.text.single_prompt import SinglePromptAgent
from src.images.stability import ImageGenerator
from src.images.image_descriptor import PostImageDescriptor
from src.utils.create_file import create_file

def colored_print(text:str, color:str='red'):
    color_dict = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'black': '\033[30m',
        'reset': '\033[0m'
    }
    print(f'{color_dict[color]}{text}{color_dict["reset"]}')


class PostAgent:
    '''
    An agent capable of make a post in any social media given rules and specifications
    '''

    def _template(self):
        #  This is a piece of your personal story: {backstory}.
        template = '''
        You are super cool content creator.
        You usually make posts under this rules: {rules}

        Your task is to create awesome social media content for your audience. The content must be 
        clear and engaging.

        Make an awesome post for {social_network} about: {post_idea}

        Keep in mind in the length of the post, follow the best practices for the platform.
        
        '''
        return template
    
    def run(self, **args):
        agent = SinglePromptAgent(template=self._template(), model='gpt-3.5-turbo')
   
        post = agent.run(
            **args,
            extract_response=False
        )
        return post

idea_to_write_about = 'How to write a good documentation'

rules = '''
        Follow the next rules to create an awesome post:
        1. Start with a phrase that captures the reader's attention according to the topic you are dealing with. A phrase that tends to: Start a debate, formulate a strong opinion, tell a truth that nobody accepts, challenge the reader, or tell him something he wants possibly to know based in your topic.

        2.  The content must be clear and readable always, it can also be:
            Explanatory: Explain something based in your knowledge, in your expertise, a list of tips to the reader, good practices, interesting facts.
            Divulgatory: Talk about something you read, about something an expert in the field says or about current news in the market that could be interesting for the objective people.
            Motivational: Talk about your backstory or someone else story that tends to be related to the audience, the people must feel identified
            Challenging: A post that puts two ideas into perspective and decides for one based on strong opinions and facts.
            Listicle: Share tools or tips based in the market objective

        3. Invite your audience to leave their opinions on the comments section.
'''

social_network = '''

'''
def main():

    manager = PostAgent()

    post = manager.run(post_idea=idea_to_write_about, social_network=social_network, rules=rules)

    colored_print(text=post)
    create_file(filename='post.txt', content=post)

    image_descriptor = PostImageDescriptor()
    image_description = image_descriptor.run(post=post, colors='just monochrome black and white')
    generator = ImageGenerator()
    generator.generate(description=image_description)

    print('---------------------------------------------------------------------------')
    colored_print('green', image_description)
    
if __name__ == '__main__':
    main()