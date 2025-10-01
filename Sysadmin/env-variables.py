"""
1. Read an environment variable
    Create a script that prints the value of HOME.
    If it does not exist, print "Not Found".
2. Set and read a custom variable
    From your shell, set APP_MODE=development.
    Write a Python script that reads APP_MODE and prints a different message for development, staging, and production.
"""

import os
import shutil

def get_home_env_var():
    env = os.environ.get('HOME')
    if not env:
        print("Environment Variable not found! ")
    return env

get_home_env_var()

def read_shell_var():
    app_mode = os.environ.get('APP_MODE')
    not_found = "Variable NOT FOUND!"
    dev = "Current app mode: DEVELOPMENT!"
    stag = "Current app mode: STAGING!"
    prod = "Current app mode: PRODUCTION!"

    if not app_mode:
        return not_found
    if app_mode == 'development':
        return dev
    if app_mode == 'staging':
        return stag
    if app_mode == 'production':
        return prod
    
read_shell_var()
        

