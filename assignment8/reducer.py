#!/usr/bin/python

import sys

dictionaryCounter = dict()

for line in sys.stdin:
    if line :
        file_path = line.strip()
        dictionaryCounter[file_path] = dictionaryCounter.get(file_path, 0) + 1
maxFile = max(dictionaryCounter, key=dictionaryCounter.get)
print maxFile + " " + str(dictionaryCounter.get(maxFile, 0))
