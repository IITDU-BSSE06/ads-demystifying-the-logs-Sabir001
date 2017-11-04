#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.strip().split("- -")
    targetPath = "/assets/js/the-associates.js"
    if len(data) == 2:
        ipAddress, rest = data
        if rest.find(targetPath) != -1:
            print "{0}".format(rest)
