#!/usr/bin/python

import sys

nine = 0
ten = 0
eleven = 0


for line in sys.stdin:
    if line.strip().find("2009") != -1 :
        nine += 1
    if line.strip().find("2010") != -1 :
        ten += 1
    if line.strip().find("2011") != -1 :
        eleven += 1

#maxNum = 0
#most = ""
#if nine > ten:
#    if nine > eleven :
#        maxNum = nine
#        most = "2009"
#    else :
#        maxNum = eleven
#        most = "2011"
#else :
#    if ten > eleven :
#        maxNum = ten
#        most = "2010"
#else :
#    maxNum = eleven
#    most = "2011"
#

most = "2009"
if ten > nine :
    most = "2010"
    if eleven > ten :
        most = "2011"
if eleven > nine :
    most = "2011"


print "2009 ", str(nine)
print "2010 ", str(ten)
print "2011 ", str(eleven)
print "Year ", most, " had most number of hits."

