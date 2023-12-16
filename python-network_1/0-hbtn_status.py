#!/usr/bin/python3
import requests

def fetch_url(url):
    """
    Fetches the content of the given URL using the requests package.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    response = requests.get(url)
    
    # Displaying the body of the response as per the specified format
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.content}")
    print(f"\t- utf8 content: {response.text}")

if __name__ == "__main__":
    fetch_url("https://alu-intranet.hbtn.io/status")
