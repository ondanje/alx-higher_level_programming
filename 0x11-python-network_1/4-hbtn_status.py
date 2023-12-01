#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using the package requests
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    content = requests.get(url)

    print('Body response:')
    print('\t- type:', type(content.text))
    print('\t- content:', content.text)
