#!/usr/bin/python3
"""
A script that takes a URL as input, sends an HTTP request to the URL, and displays the value of the X-Request-Id 
variable found in the response header.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))

