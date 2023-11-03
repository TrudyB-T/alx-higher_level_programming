#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8)"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as rep:
            info = rep.read()
            print(info.decode('utf-8'))
    except urllib.error.HTTPError as he:
        print(f"Error: {he.code}")
