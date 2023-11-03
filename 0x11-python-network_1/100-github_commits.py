#!/usr/bin/python3
"""that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys"""

if __name__ == "__main__":
    import requests
    import sys

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    reply = requests.get(url)
    comm = reply.json()

    try:
        for n in range(10):
            print(f"{comm[n]['sha']}: {comm[n]['commit']['author']['name']}")

    except IndexError:
        pass
