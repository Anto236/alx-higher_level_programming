#!/usr/bin/env python3
"""
Sends a POST request to a URL with an email as a parameter and displays the
response body (decoded in utf-8).

Usage: ./0-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode()
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
