#!/usr/bin/python3
"""
    Script that takes in a letter
    Sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":

    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    post_req = requests.post(
        'http://0.0.0.0:5000/search_user', data={"q": letter})

    try:
        data = post_req.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
