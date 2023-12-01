#!/usr/bin/python3
"""
    Script that takes in a URL
    Sends a request to the URL
    Displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    url_req = requests.get(url)

    url_status = url_req.status_code

    if url_status == requests.codes.ok:
        body = url_req.text
        print(body)
    else:
        print('Error code: {}'.format(url_status))
