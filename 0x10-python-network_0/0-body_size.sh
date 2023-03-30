#!/bin/bash
# Script using curl to display body size of response from url
curl -s "$1" | wc -c
