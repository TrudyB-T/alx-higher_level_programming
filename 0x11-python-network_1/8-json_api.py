#!/usr/bin/python3
""" that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    import sys

    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    txt = {"q": letter}

    rep = requests.post("http://0.0.0.0:5000/search_user", data=txt)

    try:
        reply = rep.json()
        if reply == {}:
            print("No result")
        else:
            print(f"[{reply.get('id')}] {reply.get('name')}")
    except ValueError:
        print("Not a valid JSON")
