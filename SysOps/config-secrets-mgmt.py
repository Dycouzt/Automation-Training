"""
1. Configuration and Secrets Management
- Write a script that encrypts/decrypts sensitive data using cryptography or Fernet.
- Parse and validate multiple YAML/JSON configuration files for missing keys or syntax errors.
- Create a dynamic environment loader that reads .env files and exports variables to the shell.
- Implement a template-based config generator using Jinja2 (e.g., render Nginx config templates).
"""

import argparse
from cryptography import fernet

def user_input():
    parser = argparse.ArgumentParser(description="Input sensitive data to be encrypted")
    parser.add_argument("Path", required=True,)