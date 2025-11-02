"""
1. Configuration and Secrets Management
- Write a script that encrypts/decrypts sensitive data using cryptography or Fernet.
- Parse and validate multiple YAML/JSON configuration files for missing keys or syntax errors.
- Create a dynamic environment loader that reads .env files and exports variables to the shell.
- Implement a template-based config generator using Jinja2 (e.g., render Nginx config templates).
"""

import argparse
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `secret.key`
    """
    return open("secret.key", "rb").read()

def encrypt_file(filename, output_file, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(output_file, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, output_file, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(output_file, "wb") as file:
        file.write(decrypted_data)

def user_input():
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt a file")
    parser.add_argument("file", help="File to encrypt/decrypt")
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the file")
    parser.add_argument("-o", "--output-file", help="Output file path")
    return parser.parse_args()

if __name__ == "__main__":
    args = user_input()
    file = args.file
    encrypt_flag = args.encrypt
    decrypt_flag = args.decrypt

    if encrypt_flag and decrypt_flag:
        raise ValueError("Please specify either encryption or decryption, not both.")

    # load key if it exists, otherwise generate it
    try:
        key = load_key()
    except FileNotFoundError:
        generate_key()
        key = load_key()

    output_file = args.output_file

    if not output_file:
        output_file = file

    if encrypt_flag:
        encrypt_file(file, output_file, key)
        print(f"File '{file}' encrypted successfully to '{output_file}'.")
    elif decrypt_flag:
        decrypt_file(file, output_file, key)
        print(f"File '{file}' decrypted successfully to '{output_file}'.")
