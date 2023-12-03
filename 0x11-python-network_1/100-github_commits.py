#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails” You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
The first argument will be the repository name
The second argument will be the owner name
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
