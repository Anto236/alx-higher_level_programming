#!/bin/bash
# Sends a POST request to a URL with email and subject parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
