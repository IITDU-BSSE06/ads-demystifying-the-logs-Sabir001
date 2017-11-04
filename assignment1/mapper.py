#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.strip().split("- -")
    if len(data) == 2:
        ipAddress, rest = data
        if ipAddress.strip() == "10.99.99.186":
            print "{0}".format(ipAddress)
