#!/usr/bin/python3
"""
This script sends a POST request to
http://0.0.0.0:5000/search_user with
a given letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    response = requests.post(url, data=data)

    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(1)

    if result:
        print("[{}] {}".format(result.get("id"), result.get("name")))
    else:
        print("No result")
