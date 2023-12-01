#!/usr/bin/python3
""" Module to fetch status from URL """
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()

    print('Body response:')
    print('\t - type: {}'.format(type(body)))
    print('\t - content: {}'.format(body))
    print('\t - utf-8 content: {}'.format(body.decode('utf-8')))
