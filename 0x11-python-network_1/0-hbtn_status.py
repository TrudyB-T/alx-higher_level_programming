#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rep:
        info = rep.read()
        print("Body response:")
        print(f"\t- type: {type(info)}")
        print(f"\t- content: {info}")
        print(f"\t- utf8 content: {info.decode('utf-8')}")
