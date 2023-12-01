#!/usr/bin/python3
"""
    Script that takes in a URL
    Sends a request to the URL
    Displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            body_dec = body.decode('utf-8')
            print(body_dec)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
