import random

def chat_interface(message="Hello, how are you!"):
        print(message)
        while True:
                user_input = input("Your message: ")
                bot_reply = generate_random_phrase()
                print(bot_reply)
def generate_random_phrase():
        words = ["apple", "banana", "cat", "dog", "elephant", "fish", "gorilla", "horse", "iguana", "jaguar", "koala", "lion", "monkey", "newt", "octopus", "penguin", "quokka", "rabbit", "sheep", "tiger", "unicorn", "vulture", "whale", "zebra"]
        return ' '.join(random.sample(words, 3))


if __name__ == "__main__":
        chat_interface()