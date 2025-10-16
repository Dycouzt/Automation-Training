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

"""
Level 2 - Input Control

1. Choices Validation:
- Script takes an argument action with allowed values start, stop, restart.
- Print a message based on the chosen action.

2. Default Value:
- Add an optional argument --env with default "dev".
- Output: Environment: dev or Environment: prod depending on input.

3. Multiple Values:
- Create a script that takes multiple filenames as input (nargs='+') and prints them line by line.
"""

def valdiate_choices():
    options = ["start", "stop", "restart"]

    parser = argparse.ArgumentParser(description="Choose action to perform")
    parser.add_argument("Action", type=str, required=True, help=f"Choose from {options}")
    args = parser.parse_args()

    if args in options:
        if args == options[0]:
            print("Starting...")
        if args == options[1]:
            print("Stopping...")
        else:
            print("Restarting...")
    else:
        raise argparse.ArgumentError

def set_environemnt():
    options = ["dev", "stag", "prod"]

    parser = argparse.ArgumentParser(description="Set Environment Stage")
    parser.add_argument("--env", default="dev", help="Set / Show current environment stage.")
    args = parser.parse_args()

    if args in options:
        if args == options[0]:
            print(f"Environment: {options[0]}")
        if args == options[1]:
            print(f"Environment: {options[1]}")
        else:
            print(f"Environment: {options[2]}")
    else:
        raise argparse.ArgumentError

def print_filenames():
    parser = argparse.ArgumentParser(description="Provide one or more filenames")
    parser.add_argument("filename", nargs="+", type=str, help="Must be a string and the file must exist")
    args = parser.parse_args()

    for file in args:
        print(f"{file}")

valdiate_choices()
set_environemnt()
print_filenames()
        
