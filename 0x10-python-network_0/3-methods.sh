#!/bin/bash
# This script takes a URL as input and displays all the HTTP methods that the server will accept.
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev

