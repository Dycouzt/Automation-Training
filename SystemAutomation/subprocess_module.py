import subprocess

# Run a simple shell command
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)

# Output the result
print(result.stdout)