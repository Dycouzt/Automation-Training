import subprocess

# Run a simple shell command
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)

# Output the result
print(result.stdout)

ping_result = subprocess.run(['ping', 'google.com'], capture_output=True, text=True)

print(ping_result.stdout)