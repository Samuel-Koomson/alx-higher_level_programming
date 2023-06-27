#!/bin/bash
# Bash script which displays all HTTP methods that the server accepts using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
