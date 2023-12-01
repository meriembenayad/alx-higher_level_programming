#!/usr/bin/python3
"""
    Script that takes in a URL
    Sends a request to the URL
    Displays the value of the X-Request-Id
    variable found in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
