#!/usr/bin/python

from urlparse import urlparse

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, hyphen1, hyphen2, date, number, req, path, protocol, status, port = data
        mainReq = req[1:]
        if mainReq :
            print mainReq
