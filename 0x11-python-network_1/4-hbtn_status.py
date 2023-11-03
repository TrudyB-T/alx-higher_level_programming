#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    rep = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(rep.text)}")
    print(f"\t- content: {rep.text}")
