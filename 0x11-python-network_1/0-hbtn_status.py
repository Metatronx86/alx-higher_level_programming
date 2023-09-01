#!/usr/bin/python3
"""A script that fetches https://intranet.hbtn.io/status and displays information about the response."""

import urllib.request

def fetch_and_display_status(url):
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')

            print("Body response:")
            print("\t- type:", type(content))  # Display the type of content (str)
            print("\t- content:", content)      # Display the content (str)

    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")

if __name__ == '__main__':
    url_to_fetch = 'https://intranet.hbtn.io/status'
    fetch_and_display_status(url_to_fetch)

