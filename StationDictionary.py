__author__ = 'rnida'
import csv
import json

statDict = {}
with open("../freeway_stations.csv", 'r') as stations:
    stationFile = csv.DictReader(stations)
    for row in stationFile:
        statDict[row["stationid"]] = row["length"]

print statDict


detDict = {}
with open("../freeway_detectors.csv", 'r') as detectors:
    detectorFile = csv .DictReader(detectors)
    for row in detectorFile:
        detDict[row["detectorid"]] = [row["stationid"],statDict[row["stationid"]]]




for key in detDict:
    print key + str(detDict[key])


with open("dictStations.json", 'w') as out:
    json.dump(detDict, out)


newdict = {}

with open("dictStations.json", 'r') as input:
    newdict = json.load(input)


print newdict


print newdict["1350"][0]