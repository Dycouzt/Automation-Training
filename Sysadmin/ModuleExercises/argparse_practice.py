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
    parser = argparse.ArgumentParser(description="Username")
    args = parser.add_argument("-h", "--help", help="Enter username.")

    print(f"Greetings, {args}")

def flag_practice():
    parser = argparse.ArgumentParser(description="verbose")
    args = parser.add_argument("-v", "--verbose", help="Turn Verbose mode on")
    
    if args:
        print(f"Verbose mode on")

def conversion_type():
    parser = argparse.ArgumentParser(description="Provide two arguments to add them")
    args = parser.add_argument("--x", "--y", nargs=2, type=int, help="Provide only two numbers")

    if args:
        x = args[0] + args[1]
        return x

get_name_parse()
flag_practice()
print(conversion_type())



