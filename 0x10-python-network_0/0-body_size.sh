#!/bin/bash
# A Bash script that takes in a URL, sends a request
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
