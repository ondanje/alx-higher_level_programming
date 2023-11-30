#!/bin/bash
# script that takes in a URL and displays all HHTTP method
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
