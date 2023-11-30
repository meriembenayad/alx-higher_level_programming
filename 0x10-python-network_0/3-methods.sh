#!/bin/bash
# Bash script that takes in URL & displays all HTTP methods the server will accept
curl -sI "@1" | grep -i Allow | cut -d ' ' -f2-
