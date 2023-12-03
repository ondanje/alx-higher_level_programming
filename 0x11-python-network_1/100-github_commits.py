#!/usr/bin/python3
"""
"""
import sys
import requests

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'\
        .format(owner, repository_name)

    response = requests.get(url)

    if response.status_code == 200:

        commits = response.json()

        count = 0
        for commit in reversed(commits):
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

            count += 1

            if count == 10:
                break
    else:
        print("Error: {}".format(response.status_code))
