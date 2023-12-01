#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST requestto the passed URL with the
email as a parameter, and displays the body of the response
"""
from urllib import request, parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = parse.urlencode({'email': email}).encode('ascii')

with request.urlopen(url, data=data) as response:
    content = response.read().decode('utf-8')

    print(content)
