#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the
GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    permit = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    rep = requests.get("https://api.github.com/user", auth=permit)
    print(rep.json().get("id"))
