#!/usr/bin/python3
"""
    Script that takes in a URL and an email
    Sends a POST request to the passed URL with the email as a parameter
    Displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data_byte = data.encode('ascii')
    req_url = urllib.request.Request(url, data_byte)

    with urllib.request.urlopen(req_url) as response:
        body = response.read()
        body_dec = body.decode('utf-8')
        print(body_dec)
