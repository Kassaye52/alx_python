#!/usr/bin/python3
""" 
3. Error code #1

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
"""
import requests
import sys

def fetch_url(url):
    """
    Fetches the content of the given URL using the requests package.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    response = requests.get(url)
    
    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_url(sys.argv[1])
    else:
        print("Please provide a URL as a command-line argument.")
