#!/usr/bin/python3
""" 
5. My GitHub!

Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
"""
import requests
import sys

def fetch_github_user_id(username, token):
    """
    Fetches the GitHub user ID using the GitHub API with Basic Authentication.

    Args:
        username (str): GitHub username.
        token (str): Personal access token for GitHub.

    Returns:
        None
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        print("Failed to fetch user data")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        fetch_github_user_id(sys.argv[1], sys.argv[2])
    else:
        print("Usage: script.py username personal_access_token")


