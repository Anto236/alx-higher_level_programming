#!/bin/bash
#sends a JSON POST request with the contents of a file to a URL and displays the response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
