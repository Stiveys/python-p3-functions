# lib/functions.py

def greet_programmer():
    """
    This function takes no arguments and prints "Hello, programmer!" to the terminal.
    """
    print("Hello, programmer!")

def greet(name):
    """
    This function takes one argument, a name, and prints "Hello, name!" to the terminal.
    """
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """
    This function takes one argument, a name, and prints "Hello, name!" to the terminal.
    If no argument is passed, it defaults to "programmer".
    """
    print(f"Hello, {name}!")

def add(num1, num2):
    """
    This function takes two numbers as arguments and returns their sum.
    """
    return num1 + num2

def halve(number):
    """
    This function takes one number as an argument and returns the number divided by two.
    """
    return number / 2