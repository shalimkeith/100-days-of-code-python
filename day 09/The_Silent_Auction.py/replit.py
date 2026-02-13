import os

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Example usage
clear()