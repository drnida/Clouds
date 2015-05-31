__author__ = 'rnida'

import csv
with open("../freeway_loopdata.csv",'r') as csvfile:

    loop = csv.reader(csvfile)
    loop.next()
    for line in loop:
        if line[0] == "1350":
            print line