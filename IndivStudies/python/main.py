from itertools import *
import csv
file = open('output1Real.csv', 'a')
fileWriter = csv.writer(file)

fileWriter.writerow(['N', 'Num of Working', 'Minimal Required'])
# rulerLength = input("Enter a ruler length: ")

for rulerLength in xrange(27, 29):
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

        if tickDiffsPossible >= rulerLength:
            for tickSet in possibleTicksSets:

                #print "     Testing set: ", tickSet
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
                    #print "found working set for ", rulerLength
                    if found is False:
                        found = True
                        minimalTicksRequired = len(tickSet) - 2
                else:
                    i = 0
                        # print "     Does Not Work."
        # else:
        #     print "     None of these combinations will work as they do not contain a minimal amount of elements to account " \
        #           "for all the differences"
    fileWriter.writerow([rulerLength, worksCounter, minimalTicksRequired])