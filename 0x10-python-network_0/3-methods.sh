#!/bin/bash
# Script Takes URL and displays methods that are accepted
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
