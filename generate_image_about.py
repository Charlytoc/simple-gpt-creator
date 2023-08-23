import os
from src.images.stability import ImageGenerator


def generate_image(image_description: str):
    imaginator = ImageGenerator()
    imaginator.generate(description=image_description)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
            image_description = sys.argv[1]
            generate_image(image_description)
    else:
            print("No text to translate provided.")
