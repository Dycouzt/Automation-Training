import subprocess
import os
from dotenv import load_dotenv

"""
1. Read an environment variable
    Create a script that prints the value of HOME.
    If it does not exist, print "Not Found".
2. Set and read a custom variable
    From your shell, set APP_MODE=development.
    Write a Python script that reads APP_MODE and prints a different message for development, staging, and production.
"""



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

"""
3. Use environment variables with defaults
    Write a script that reads DB_HOST.
    If it is not defined, fall back to "localhost".
4. Export multiple variables and consume them
    Set three variables in your shell: DB_USER, DB_PASS, DB_NAME.
    Write a script that connects these into a connection string:
    mysql://<DB_USER>:<DB_PASS>@localhost/<DB_NAME>.
5. Update environment variables from Python
    In a script, temporarily set MY_TEMP_PATH=/tmp/test.
    Spawn a subprocess (using subprocess.run) that prints MY_TEMP_PATH.
    Verify that the child process sees the updated variable.
"""


def db_fallback():
    DB_HOST = os.environ.get('VAR', 'localhost')

    print(f"DB_HOST: {DB_HOST}")


def conn_str():
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_name = os.environ.get('DB_NAME')

    print(f"mysql://{db_user}:{db_pass}@localhost/{db_name}")

def temp_update_var():
    os.environ["MY_TEMP_PATH"] = "/tmp/test"
    ps = subprocess.run("echo $MY_TEMP_PATH", shell=True, capture_output=True, text=True)
    print(ps.stdout.strip())

db_fallback()
conn_str()
temp_update_var()

"""
6. Secure variable access
    Store SECRET_KEY in an environment variable.
    Write a script that loads it, but raises an exception if it’s missing or empty.
7. Dotenv integration
    Create a .env file with multiple variables.
    Use python-dotenv to load them into the environment.
    Verify your script reads them as if they were exported normally.
8. Variable scoping test
    Write a Python script that sets a variable with os.environ.
    Spawn two subprocesses: one using inherit_env=True, another with env={}.
    Show the difference in output.
"""

def secret_key():
    try:
        secret = os.environ.get('SECRET_KEY')
        print(f"SECRET_KEY: {secret}")

    except Exception as e:
        print("Variable not found.")

def dotenv():
    load_dotenv()

    db_host = os.environ.get('DB_HOST')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')

    print(f"DB_HOST: {db_host}")
    print(f"DB_USER: {db_user}")
    print(f"DB_PASS: {db_pass}")


def var_scoping():
    # Set variable in current process environment
    os.environ["MY_VAR"] = "visible_in_child"

    # Subprocess inherits environment by default
    print("---- Subprocess with inherited environment ----")
    subprocess.run(["python3", "-c", "import os; print(os.getenv('MY_VAR'))"])

    # Subprocess with empty environment (variable not passed down)
    print("---- Subprocess with cleared environment ----")
    subprocess.run(["python3", "-c", "import os; print(os.getenv('MY_VAR'))"], env={})

secret_key()
dotenv()
var_scoping()
