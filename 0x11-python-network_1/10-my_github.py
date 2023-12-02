#!/usr/bin/python3
"""
    Script that takes your GitHub credentials (username and password)
    Uses the GitHub API to display your id
"""
import sys
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":

    # input username & password
    username = sys.argv[1]
    password = sys.argv[2]

    # Basic Authentication with username and password
    auth = HTTPBasicAuth(username, password)

    # Send a GET request to the GitHub API to get the user info
    resp_url = requests.get("https://api.github.com/user", auth=auth)

    try:
        data = resp_url.json()
        if 'id' in data:
            print(data['id'])
        else:
            print('None')
    except ValueError:
        print('Not a valid JSON')
