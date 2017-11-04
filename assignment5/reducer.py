#!/usr/bin/python

import sys

dictionaryCounter = dict()

for line in sys.stdin:
	file_path = line.strip()
	dictionaryCounter[file_path] = dictionaryCounter.get(file_path, 0) + 1

print len(dictionaryCounter)
