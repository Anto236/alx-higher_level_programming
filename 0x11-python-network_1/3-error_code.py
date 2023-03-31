#!/usr/bin/env python3

"""
This module takes a URL, sends a request to the
URL and displays the body of the response.
"""

from urllib import request, error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {}".format(e.code))
