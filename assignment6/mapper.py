#!/usr/bin/python


import sys

for line in sys.stdin:
    data = line.strip().split("- -")
    if len(data) == 2:
        ipAddress, rest = data
        stripedRestData = rest.strip()
        if stripedRestData.find("2009") != -1 :
            print("2009")
        if stripedRestData.find("2010") != -1 :
            print("2010")
        if stripedRestData.find("2011") != -1 :
            print(2011)
