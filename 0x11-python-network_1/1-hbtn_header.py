#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays X-Request-Id variable in header
"""
import sys
import urllib.request

if __name__ == "__main__":
    URL = sys.argv[1]
    request = urllib.request.Request(URL)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
