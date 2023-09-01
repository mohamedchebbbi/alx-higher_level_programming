#!/usr/bin/python3
"""
1. Response header value #0
"""
import urllib.request
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    request = urllib.request.Request(URL)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
