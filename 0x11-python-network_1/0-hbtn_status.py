#!/usr/bin/python3
""" Script to fetches Body """
import urllib.request

if __name__ == "__main__":
    """ fetch the body of the response """
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()

        print('Body response:')
        print('\t - type: {}'.format(type(body)))
        print('\t - content: {}'.format(body))
        print('\t - utf-8 content: {}'.format(body.decode('utf-8')))
