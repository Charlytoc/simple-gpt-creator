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
