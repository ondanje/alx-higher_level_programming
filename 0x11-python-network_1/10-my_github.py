#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id You must use Basic Authentication
with a personal access token as password to access to your information
(only read:user permission is needed)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    basic = HTTPBasicAuth(username, password)

    response = requests.get('https://api.github.com/user', auth=basic)

    if response.status_code == 200:
        user_id = response.json().get('id')

        print(user_id)
    else:
        print(None)
