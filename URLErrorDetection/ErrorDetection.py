"""
This is a simple URL error detection script that implements the request module focused on networking in python.
- Takes a list of URLs.
- Sends a GET request to each.
Prints:
- URL
- Status code
- “Working” if 200
- “Broken” otherwise
"""
import requests


def error_detection(urls):
    for url in urls:
        url = url.strip()  # Remove leading/trailing spaces
        try:
            response = requests.get(url)
            status = response.status_code
            print(f"URL: {url}")
            if status == 200:
                print("Status Code:", status)
                print("URL is up and working!")
            else:
                print("Status Code:", status)
                print("URL is currently down or not working...")
        except requests.exceptions.RequestException as e:
            print(f" Error checking URL: {url}")
            print(f"Reason: {e}")
        print("-" * 40)


def main():
    print("Enter URLs to check separated by a comma (','):")
    user_input = input("--> ")

    # Split input into list of cleaned URLs
    urls = [url.strip() for url in user_input.split(",") if url.strip()]

    if urls:
        error_detection(urls)
    else:
        print("No valid URLs provided.")


if __name__ == "__main__":
    main()

