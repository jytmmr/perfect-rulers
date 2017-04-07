from joblib import Parallel, delayed
import csv
from itertools import *

file = open('TickData2.csv', 'w')
dataArray = []
fileWriter = csv.writer(file)
fileWriter.writerow(['N', 'Minimal Required', 'First Working Set'])
global numberOfWorkingMinimalSets
numberOfWorkingMinimalSets = 0
global minimalFound
minimalFound = False

def writeResults(results):

    fileWriter.writerow(results)
    dataArray.append(results)

def tester(tickSet, markArray):
    if ((rulerLength -1) in tickSet) or (1 in tickSet):
        if(((rulerLength -1) in tickSet) and (1 in tickSet)) or ((rulerLength-2 in tickSet)) or (2 in tickSet):
            tickSet += (0, rulerLength)
            combosOfTwo = combinations(tickSet, 2)
            combosOfTwo = [y for y in combosOfTwo]
            tempMarkArray = []
            tempMarkArray += markArray
            for combo in combosOfTwo:
                diff = abs(combo[1] - combo[0])
                if diff in tempMarkArray:
                    tempMarkArray.remove(diff)
                if len(tempMarkArray) == 0:
                    break
            if len(tempMarkArray) == 0:
                global numberOfWorkingMinimalSets
                numberOfWorkingMinimalSets += 1;

for rulerLength in xrange(41,43):
    print rulerLength
    markArray = []
    for x in xrange(1, rulerLength):
        markArray.append(x)
    minimalTicksRequired = 0
    minimalTickSet = []
    for tickMark in markArray:

        if numberOfWorkingMinimalSets > 0:
            minimalFound = True
            minimalTicksRequired = tickMark -1
            break
        print "testing markArray of size" , tickMark
        possibleTicksSets = [y for y in combinations(markArray, tickMark)]
        tickDiffsPossible = ((tickMark+1)*(tickMark + 2))/2
        if tickDiffsPossible >= rulerLength:
            Parallel(n_jobs=100, backend="threading")(delayed(tester)(tickSet, markArray) for tickSet in possibleTicksSets)
    if numberOfWorkingMinimalSets > 0:
        print "writing results for " , rulerLength
        writeResults([rulerLength, minimalTicksRequired, numberOfWorkingMinimalSets])
        global numberOfWorkingMinimalSets
        numberOfWorkingMinimalSets = 0











print "here", dataArray
# for item in dataArray:
#     fileWriter.writerow(item)







