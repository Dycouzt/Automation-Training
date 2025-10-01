"""
1. Read an environment variable
    Create a script that prints the value of HOME.
    If it does not exist, print "Not Found".
2. Set and read a custom variable
    From your shell, set APP_MODE=development.
    Write a Python script that reads APP_MODE and prints a different message for development, staging, and production.
"""
import os

def get_home_env_var():
    env = os.environ.get('HOME')
    if env:
        print(f"HOME: {env}")
    else:
        print("HOME environment variable not found!")

def read_shell_var():
    app_mode = os.environ.get('APP_MODE')
    if not app_mode:
        print("APP_MODE not found")
    elif app_mode == 'development':
        print("Current app mode: DEVELOPMENT")
    elif app_mode == 'staging':
        print("Current app mode: STAGING")
    elif app_mode == 'production':
        print("Current app mode: PRODUCTION")
    else:
        print(f"APP_MODE has unknown value: {app_mode}")

get_home_env_var()
read_shell_var()

