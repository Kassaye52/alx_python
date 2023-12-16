#!/usr/bin/python3
""" 
4. Search API

Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

def send_post_request(url, letter):
    """
    Sends a POST request to the specified URL with the given letter as a parameter.

    Args:
        url (str): The URL to which the POST request is sent.
        letter (str): The letter to send as a parameter.

    Returns:
        None
    """
    response = requests.post(url, data={'q': letter})

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    send_post_request("http://0.0.0.0:5000/search_user", letter)


