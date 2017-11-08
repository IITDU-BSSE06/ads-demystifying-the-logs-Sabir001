#!/usr/bin/python

from urlparse import urlparse

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, hyphen1, hyphen2, date, number, req, filePath, protocol, status, port = data
        rightSide = filePath
        file_path = urlparse(rightSide.split()[0]).path
        if file_path:
            print str(file_path)
