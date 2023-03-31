#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status
and displays the body of the response with proper formatting
"""

from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf8_content))
