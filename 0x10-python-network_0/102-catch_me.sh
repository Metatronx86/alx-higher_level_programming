#!/bin/bash

# Set the URL
url="http://0.0.0.0:5000/catch_me"

# Make a POST request with a custom request header
curl -s -X POST "$url" -H "X-HolbertonSchool-User-Id: 98"

