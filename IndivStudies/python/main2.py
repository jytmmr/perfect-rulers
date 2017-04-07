from itertools import *
import csv
file = open('output2.csv', 'a')
fileWriter = csv.writer(file)

fileWriter.writerow(['N', 'Minimal Required', 'First Working Set'])
# rulerLength = input("Enter a ruler length: ")

for rulerLength in xrange(37, 46):
    print rulerLength
    markArray = []
    for x in xrange(1, rulerLength):
        markArray.append(x)
    #print "Testing where n = ", rulerLength
    minimalTicksRequired = 0
    found = False
    worksCounter = 0
    for tickMark in markArray:
        # print "Here are our combinations of size: ", tickMark
        # These are all of the combinations
        possibleTicksSets = combinations(markArray, tickMark)
        possibleTicksSets = [y for y in possibleTicksSets]
        #print "Possible ticksets ", possibleTicksSets
        tickDiffsPossible = ((tickMark+1)*(tickMark + 2))/2
        # print "Number of tickDifferences possible for current size: ", tickDiffsPossible
        minimalFound = False
        if tickDiffsPossible >= rulerLength:
            for tickSet in possibleTicksSets:
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
                    worksCounter += 1
                    if found is False:
                        found = True
                        minimalTicksRequired = len(tickSet) - 2
                        minimalFound = True
                        fileWriter.writerow([rulerLength, minimalTicksRequired, tickSet])
                        break
                if minimalFound:
                    break
        if minimalFound:
            break
