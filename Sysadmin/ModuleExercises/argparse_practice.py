# Practice of the argparse module in python.

import argparse

""" 
Level 1 - Basics

1. Hello Argument:
- Write a script that takes one positional argument name and prints Hello, <name>.
- Add --help to show description and usage.
- Example: python script.py Diego → Hello, Diego

2. Flag Practice:
- Create a script that accepts --verbose and prints “Verbose mode ON” only when the flag is passed.

3. Type Conversion:
- Write a script that takes two integers (--x, --y) and prints their sum.
- Validate that both are integers using type=int.

"""

def get_name_parse():
    parser = argparse.ArgumentParser(description="Username input")
    parser.add_argument("username", help="Enter username")  # positional argument
    args = parser.parse_args()  # parse command-line arguments
    print(f"Greetings, {args.username}")

def flag_practice():
    parser = argparse.ArgumentParser(description="Verbose flag example")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode ON")
    else:
        print("Verbose mode OFF")

def conversion_type():
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("--x", type=int, required=True, help="First number")
    parser.add_argument("--y", type=int, required=True, help="Second number")
    args = parser.parse_args()

    result = args.x + args.y
    print(f"Sum: {result}")
    return result


