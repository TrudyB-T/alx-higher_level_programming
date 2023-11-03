#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of
the response"""

if __name__ == "__main__":
    import requests
    import sys

    rep = requests.get(sys.argv[1])
    if rep.status_code >= 400:
         print(f"Error code: {rep.status_code}")
    else:
        print(rep.text)
