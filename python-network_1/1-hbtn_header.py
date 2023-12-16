#!/usr/bin/python3
""" 
1. Response header value #1

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

def fetch_x_request_id(url):
    """
    Fetches the URL and prints the value of 'X-Request-Id' from the response headers.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    response = requests.get(url)

    # Get 'X-Request-Id' from response headers
    x_request_id = response.headers.get('X-Request-Id')
    
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_x_request_id(sys.argv[1])
    else:
        print("Please provide a URL as a command-line argument.")
