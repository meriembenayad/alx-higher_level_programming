#!/usr/bin/python3
"""
    Script that takes in a URL and an email address
    Sends a POST request to the passed URL with the email as a parameter
    Finally displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    url_req = requests.post(url, email)

    print(url_req.text)
