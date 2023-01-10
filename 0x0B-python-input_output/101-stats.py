#!/usr/bin/python3
""" Module to print status code """
import sys
from collections import defaultdict

total_size = 0
status_codes = defaultdict(int)

try:
    for i, line in enumerate(sys.stdin, 1):
        fields = line.strip().split()
        if len(fields) == 5:
            status = fields[-2]
            size = int(fields[-1])
            total_size += size
            status_codes[status] += 1
            if i % 10 == 0:
                print("Total file size: ", total_size)
                print("Number of lines by status code:")
                for status in sorted(status_codes.keys()):
                    print(f"{status}: {status_codes[status]}")
except KeyboardInterrupt:
    print("Total file size: ", total_size)
    print("Number of lines by status code:")
    for status in sorted(status_codes.keys()):
        print(f"{status}: {status_codes[status]}")

