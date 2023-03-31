#!/usr/bin/python3

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
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print(f'Error code: {}'.format(e.code))
