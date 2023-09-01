#!/usr/bin/python3
"""
A script that:
- Takes a URL and an email address as input.
- Sends a POST request to the specified URL with the email as a parameter.
- Displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)

