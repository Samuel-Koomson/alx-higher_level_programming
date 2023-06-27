#!/bin/bash
# Bash script that takes, sends request to URL, and displays size of the body of the response
curl -s "$1" | wc -c
