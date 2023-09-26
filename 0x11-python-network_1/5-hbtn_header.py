#!/usr/bin/python3
"""
A script that fetches the content of https://intranet.hbtn.io/status using the requests library
and displays information about the response.
"""
import requests

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))

