from joblib import Parallel, delayed
import csv
from itertools import *

file = open('TickOutput.csv', 'a')
dataArray = []
fileWriter = csv.writer(file)
# fileWriter.writerow(['N', 'Minimal Required', 'First Working Set'])
def writeResults(results):
    print "here"

    fileWriter.writerow(results)
    dataArray.append(results)

def looper(rulerLength):
    print rulerLength
    fileWriter.writerow(["Ruler Lenth ", rulerLength])
    markArray = []
    for x in xrange(1, rulerLength):
        markArray.append(x)
    #print "Testing where n = ", rulerLength
    minimalTicksRequired = 0
    minimalfound = False
    minimalTickSet = []
    numberOfWorkingMinimalSets = 0
    for tickMark in markArray:

        if minimalfound is True:
            break
        possibleTicksSets = [y for y in combinations(markArray, tickMark)]
        tickDiffsPossible = ((tickMark+1)*(tickMark + 2))/2
        if tickDiffsPossible >= rulerLength:

            for tickSet in possibleTicksSets:
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
                            numberOfWorkingMinimalSets += 1;
                            fileWriter.writerow(["  " ,tickSet])
                            if minimalfound is False:
                                minimalfound = True
                                minimalTickSet = tickSet
                                minimalTicksRequired = len(tickSet) - 2
                                print "minimal ticks", minimalTicksRequired
    #writeResults([rulerLength, minimalTicksRequired, minimalTickSet, numberOfWorkingMinimalSets])



Parallel(n_jobs=70, backend="threading")(delayed(looper)(i) for i in xrange(2,7))


print "", dataArray
# for item in dataArray:
#     fileWriter.writerow(item)



