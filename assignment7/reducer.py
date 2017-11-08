#!/usr/bin/python

import sys

dictionaryCounter = dict()

for line in sys.stdin:
    if line :
        reqType = line.strip()
        dictionaryCounter[reqType] = dictionaryCounter.get(reqType, 0) + 1

print len(dictionaryCounter), " types of file was there."
for req in dictionaryCounter :
    print req, dictionaryCounter[req]
