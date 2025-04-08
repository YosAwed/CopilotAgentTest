def validate_input(user_input):
    if user_input not in ['X', 'O']:
        raise ValueError("Input must be 'X' or 'O'")
    return user_input

def display_message(message):
    print(message)

def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')