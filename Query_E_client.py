__author__ = 'rnida'

import json
import pprint
import urllib2


response = urllib2.urlopen('http://abovethecloud.iriscouch.com/cumulonimbus/_design/E_205_NB_TRAVEL_TIME_79_46/_view/E_205_NB_TRAVEL_TIME_79_46?group=true')
html = response.read()

#print html

dump = json.loads(html)
# with open("dump.json", 'r') as input:
#     dump = json.load(input)


print json.dumps(dump)


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dump)
total = 0
for x in dump["rows"]:
    if x["key"][1] == "AM":
        if x["value"]["aveStationTravTime"]:
            total += x["value"]["aveStationTravTime"]
            print str(x["key"]) + str(total)


print "AM Total" + str(total * 60)


total = 0
for x in dump["rows"]:
    if x["key"][1] == "PM":
        if x["value"]["aveStationTravTime"]:
            total += x["value"]["aveStationTravTime"]
            print str(x["key"]) + str(total)


print "PM Total" + str(total * 60)