__author__ = 'rnida'


import csv
import json
count = 0

f = open("smallLoops.json", 'w')

f.write('{\n\t"docs": [\n')

with open("dictStations.json", 'r') as input:
    detector = json.load(input)

error = set()

with open("../freeway_loopdata.csv",'r') as csvfile:

    loop = csv.reader(csvfile)
    loop.next()
    for line in loop:
        if line[1].split()[0] == "2011-09-21" or line[1].split()[0] == "2011-09-22":
            try:
                print line[1].split()[0]
                string =( '      {\n         "detectorid":' + '"' + line[0] +'"' +',\n'
                 + '         "stationid":' + '"' + detector[line[0]][0] + '"' + ',\n'
                 + '         "length":' + '"' + detector[line[0]][1] + '"' + ',\n'
                 + '         "starttime":' + '"' + line[1] +'"' + ',\n'
                 + '         "volume":' + '"' + line[2] +'"' + ',\n'
                 + '         "speed":' + '"' + line[3] +'"' + ',\n'
                 + '         "occupancy":' + '"' + line[4] +'"' + ',\n'
                 + '         "status":' + '"' + line[5] +'"' + ',\n'
                 + '         "dqflags":' + '"' + line[6] +'"' + '\n            },\n' )

                if(count > 2000):
                    break
                count += 1
                f.write(string)
            except:
                error.add(line[0])
                pass
       # if count > 10:
        #    break


f.write("           {}\n")
f.write('   ]\n}\n')

print error