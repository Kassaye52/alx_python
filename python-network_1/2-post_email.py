#!/usr/bin/python3
""" 
2. POST an email #1

Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""

import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the given email.

    Args:
        url (str): The URL to which the POST request is sent.
        email (str): The email address to send as a parameter.

    Returns:
        None
    """
    response = requests.post(url, data={'email': email})

    # Display the body of the response
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        send_post_request(sys.argv[1], sys.argv[2])
    else:
        print("Usage: script.py URL email")
