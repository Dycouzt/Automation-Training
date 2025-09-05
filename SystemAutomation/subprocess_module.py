# Topic Review subprocess module.

import subprocess

subprocess.run() # Simplest way to run a command. Waits until command finishes and returns a CompletedProcess object.

result = subprocess.run(["echo", "Hello"], capture_output=True, text=True) # example.
print(result.stdout) # expected output: "Hello".