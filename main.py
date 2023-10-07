
from src.text.single_prompt import SinglePromptAgent
from src.images.stability import ImageGenerator
from src.utils.create_file import create_file
from src.utils.colored_print import colored_print


def generate_post_about(about:str, number_of_words:int=300):
    template = """You are an experienced copy writter.
    You have a lot of information in a variety of field.
    You need to write a post about: {about}

    With an extension of {number_of_words} words.

    Use a kind and intellectual language.
    Write the post in markdown format, the first h1 must be the title.
    """
    agent = SinglePromptAgent(template=template, 
                              temperature=0.2, 
                              model="gpt-3.5-turbo")
    return agent.run(about=about, 
                     number_of_words=number_of_words)

def generate_image_description_for_post(post:str, 
                                        style:str="digital art", 
                                        number_of_words:int=100):
    template = """As an experienced artist, you have created a lot of awesome
    artistic works. You know how to write a good description of an art composition.

    Write an image description of no more than {number_of_words} words for the next post:
    
    {post}
    
    The style of the image must be: {style}

    Write just the image description as a composition using descriptive word.
    Describe the scene, the characters if needed, colors, shapes and textures.
    Use words to describe the scene but never more than the needed {number_of_words} words.
    """
    agent = SinglePromptAgent(template=template, 
                              temperature=0.8, 
                              model="gpt-3.5-turbo")
    return agent.run(post=post, 
                     style=style, 
                     number_of_words=number_of_words)


def slugify_with_ai(about:str):
    template="""We need to create a file name based in this text: "{about}"

    Your task is to return a slug for the text that is
    consistent and is related to the text itself.
    
    We want to use that slug as a filename, it will be used for images and a text file.
    
    Avoid further comments, just make your task.
    Return just the slug itself separated with dashes like:
    
    this-will-be-a-slug
    """
    agent = SinglePromptAgent(template=template, 
                              temperature=0)
    return agent.run(about=about)

def main():
    colored_print("Thinking...")
    about = "Writting a song about the universe of Harry Potter"

    slug = slugify_with_ai(about)


    colored_print(f'Slug: {slug}', "yellow")
    colored_print(f"I will generate a post about {about}")

    post = generate_post_about(about=about)

    colored_print("Saving post in output directory...")
    create_file(filename=f'{slug}.md', 
                content=post)

    colored_print(post, "blue")
    image_for_post = generate_image_description_for_post(post)

    colored_print(f"Generating image based in the description:\n\n{image_for_post}", "green")

    generator = ImageGenerator(title=slug, 
                               samples=2)
    
    generator.generate(description=image_for_post)
    
if __name__ == '__main__':
    main()