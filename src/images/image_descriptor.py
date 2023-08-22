from src.text.single_prompt import SinglePromptAgent
from src.images.stability import ImageGenerator


class PostImageDescriptor:
    def __init__(self, temperature: int = 0):
        self.temperature = temperature
    def _template(self):
        template = '''
        You are an artist with an extensive background in {desired_art}.

        Your task is to create a description of an image that can be used
        for a post in social media.

        This is the post: {post}

        Create a description including colors, objects, and the relevant information
        to create the image. The image must be clean and minimalistic but related
        to the post.

        The description must be no more than {number_of_words} words.

        Try to describe the content of the image in the best way. Use just this colors: {colors}

        Don't include anything about text in the description, just objects, colors, background and scene.

        Try to follow this format:

        background: (include color, shapes, something minimalistic)
        objects: (describe the objects present in the image and their colors)
        scene: (describe the scene mentioning what each object does)
      
    
        '''
        return template
    def run(self, post: str, desired_art: str = 'digital art and NFTs', number_of_words: int = 100, colors: str = 'any colors'):
        agent = SinglePromptAgent(template=self._template(), model='gpt-3.5-turbo', temperature=self.temperature)
   
        image_description = agent.run(
            number_of_words=number_of_words,
            desired_art=desired_art,
            colors=colors,
            extract_response=False,
            post=post
        )
        return image_description

def main():
    post = '''
    Can you imagine what it is like to know nothing?

    He was reading about animism, which is a belief that basically everything has a soul. From animals, to animated objects, to manifestations of nature. On Wikipedia it basically tells you how that conclusion was reached throughout the article.

    And now comes the relationship of the above with the title, what would you think if you don't know anything and you have a dream? This requires a blank mind. When I say not knowing anything, I mean that there is no language, I mean not knowing what life or death means, you are an animal that only lives to eat, sleep, reproduce.

    Imagine being self-aware for the first time in your life, like when a baby is born in a movie. Suddenly you start to realize that you have 5 fingers, that you have eyes, you feel the ground, gravity, it's wonderful.

    The wonderful thing about thinking about what it's like to know nothing is knowing that you know. Is that what makes us human... Isn't it? Having a unique knowledge base, being aware of everything... But why is that so? What would have happened if our ancestors, instead of forming a database in an X way, did it in a Y way? Suppose we can think of it by having a language. Today what humanity knows is based on ideas that we accept as true. We take the existence of gravity as certain, and for us it is a physical phenomenon, we invented the idea of "physics", what would have happened if we called it "air"? It is the air that pushes you down, the air is made up of all our ideas, and we can only fly when we stop thinking, that day we will be part of someone else's idea.

    The above is not to say that I believe that, but what if I do? And 30 thousand years ago I am the father of a child and I tell him those ideas? That child would believe me because I am his father. And if for some reason that spread to all individuals of the species, today that would be what is taken as true.

    We cannot know if our knowledge is real, because we do not have another perspective that is somehow superior. And even if it existed, how could we know that this is the real one and not the sample? It is like the perspective of our cat with us, does that cat know that it is a cat? Do you know that our species has traveled into space? There is no way that he can communicate with us, unless he continues to evolve until he develops a language and thoughts compatible with ours.

    If now the cat is us, what is beyond our knowledge? Sadly, according to our knowledge, we can only continue to evolve until it can be compatible with another.

    For me, language is one of the maxims of our evolution, and a superior intelligence would also have a superior language. To answer the question of the dream... Well, invent, I could think that there is something beyond death, for example (although this would imply that I put a meaning to death).

    If you got this far and managed to think about what it's like to know nothing, you'll realize everything you know, or think you know.
    '''
    image_descriptor =PostImageDescriptor()
    image_description = image_descriptor.run(post=post, desired_art='renaissance art', colors='white, black, burgundy')
    image_generator = ImageGenerator()
    print(image_description)
    image_generator.generate(description=image_description)

if __name__ == '__main__':
    main()