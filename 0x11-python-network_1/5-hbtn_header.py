#!/usr/bin/python3
"""
    Script that takes in a URL
    Sends a request to the URL
    Displays the value of the variable 'X-Request-Id' in the response header
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    headers = url.headers['X-Request-Id']

    print(headers)
