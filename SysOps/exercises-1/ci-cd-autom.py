"""
3. CI/CD and Container Automation
- Automate a Docker image build and push to registry using Python.
- Write a script to scan Dockerfiles for insecure instructions (e.g., latest tags, root user).
- Parse Jenkins or GitHub Actions build logs to extract metrics (success/failure counts, duration).
- Implement a Git repo monitor that detects new commits and triggers custom actions.
"""
import docker
import os
import re

# 1. Automate a Docker image build and push to a registry.
def build_and_push_docker_image(image_name, registry, tag="latest"):
    """
    Builds a Docker image from a Dockerfile in the current directory and pushes it to a registry.

    Args:
        image_name (str): The name of the Docker image.
        registry (str): The Docker registry to push the image to.
        tag (str, optional): The tag for the image. Defaults to "latest".
    """
    try:
        client = docker.from_env()
        image, build_log = client.images.build(path=".", tag=f"{image_name}:{tag}")
        print("Image built successfully:")
        for line in build_log:
            if 'stream' in line:
                print(line['stream'].strip())

        # Tag the image for the registry
        registry_image_name = f"{registry}/{image_name}:{tag}"
        image.tag(registry_image_name)

        # Push the image to the registry
        print(f"Pushing image to {registry_image_name}...")
        push_log = client.images.push(registry_image_name, stream=True, decode=True)
        for line in push_log:
            print(line)

        print("Image pushed successfully.")

    except docker.errors.BuildError as e:
        print(f"Error building image: {e}")
    except docker.errors.APIError as e:
        print(f"Error with Docker API: {e}")

# Example usage (replace with your registry and image name)
# build_and_push_docker_image("my-python-app", "your-docker-registry")

# 2. Scan Dockerfiles for insecure instructions.
def scan_dockerfile(dockerfile_path="Dockerfile"):
    """
    Scans a Dockerfile for insecure instructions.

    Args:
        dockerfile_path (str, optional): The path to the Dockerfile. Defaults to "Dockerfile".
    """
    insecure_instructions = []
    try:
        with open(dockerfile_path, "r") as f:
            for line in f:
                if line.strip().startswith("FROM") and ":latest" in line:
                    insecure_instructions.append(f"Using 'latest' tag in FROM instruction: {line.strip()}")
                if line.strip().lower() == "user root":
                    insecure_instructions.append(f"Running as root user: {line.strip()}")
    except FileNotFoundError:
        print(f"Dockerfile not found at {dockerfile_path}")
        return

    if insecure_instructions:
        print("Insecure instructions found:")
        for instruction in insecure_instructions:
            print(f"- {instruction}")
    else:
        print("No insecure instructions found.")

# Example usage
# scan_dockerfile()

# 3. Parse Jenkins or GitHub Actions build logs to extract metrics.
def parse_build_logs(log_file_path):
    """
    Parses build logs from Jenkins or GitHub Actions to extract metrics.

    Args:
        log_file_path (str): The path to the log file.
    """
    metrics = {
        "success": 0,
        "failure": 0,
        "duration": None
    }
    try:
        with open(log_file_path, "r") as f:
            log_content = f.read()

            # Jenkins log parsing
            if "Finished: SUCCESS" in log_content:
                metrics["success"] = 1
            elif "Finished: FAILURE" in log_content:
                metrics["failure"] = 1

            duration_match = re.search(r"Build duration: (\d+ sec)", log_content)
            if duration_match:
                metrics["duration"] = duration_match.group(1)

            # GitHub Actions log parsing
            if "Job complete: Success" in log_content:
                metrics["success"] = 1
            elif "Job complete: Failure" in log_content:
                metrics["failure"] = 1

            duration_match = re.search(r"Total execution time: (\d+s)", log_content)
            if duration_match:
                metrics["duration"] = duration_match.group(1)

    except FileNotFoundError:
        print(f"Log file not found at {log_file_path}")
        return

    print(f"Metrics for {log_file_path}:")
    print(f"- Success: {metrics['success']}")
    print(f"- Failure: {metrics['failure']}")
    print(f"- Duration: {metrics['duration']}")

# Example usage
# parse_build_logs("jenkins.log")
# parse_build_logs("github_actions.log")
