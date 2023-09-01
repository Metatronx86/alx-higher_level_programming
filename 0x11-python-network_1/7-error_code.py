#!/usr/bin/python3
"""
A script that:
- Takes a URL as input.
- Sends a request to the specified URL.
- Displays the body of the response.
- If the response status code is 400 or higher, it displays an error code.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)

