# Practice of the argparse module in python.

import argparse
from pathlib import Path

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

def choice_validation():
    parser = argparse.ArgumentParser(description="Choice Validation from choices")
    parser.add_argument("Action", required=True, options=["Start", "Stop", "Restart"], help="Choose a valid option")
    args = parser.parse_args()

    if args.action == "Start":
        print(f"Starting...")
    if args.action == "Stop":
        print(f"Stopping...")
    if args.action == "Restart":
        print(f"Restarting...")

def def_value():
    parser = argparse.ArgumentParser(description="Get Project Environment")
    parser.add_argument("-env", "--environment", default="dev", options=["dev", "stag", "prod"], help="Set project environment")
    args = parser.parse_args()

    if args.env:
        print(f"Environment: {args.env}")
    else:
        raise argparse.ArgumentErrora

def multiple_values():
    parser = argparse.ArgumentParser(description="Print Multiple filename variables line by line")
    parser.add_argument("filename", nargs="+", type=str, help="Provide a valid filename name to look for.")
    p = Path(parser.add_argument("pathname", default=".", type=str, help="Input one or more filenames"))
    args = parser.parse_args()

    if args.filename and args.pathname:
        for file in p:
            print(file)

if __name__ == "__main__":
    get_name_parse()
    flag_practice()
    conversion_type()
    choice_validation()
    def_value()
    multiple_values()