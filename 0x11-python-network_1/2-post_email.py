#!/usr/bin/python3
"""that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    fact = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")

    with urllib.request.urlopen(sys.argv[1], fact) as rep:
        info = rep.read()
        print(info.decode('utf-8'))
