#!/usr/bin/python3
"""
A script that:
- Takes a letter as input.
- Sends a POST request to 'http://0.0.0.0:5000/search_user' with the letter as a parameter.
- Handles the response:
  - If the response contains valid JSON data, it extracts and displays the 'id' and 'name' values.
  - If the response is empty, it prints "No result."
  - If the response is not valid JSON, it prints "Not a valid JSON."
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

