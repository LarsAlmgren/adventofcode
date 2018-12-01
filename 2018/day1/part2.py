from sets import Set

frequencies = [line.rstrip('\n') for line in open('data1.txt')]

def getNum(counter):
    return counter % len(frequencies)

currentFrequency = 0
seenFrequencies = Set([currentFrequency])
counter = 0

while True:
    frequency = frequencies[getNum(counter)]
    counter += 1

    currentFrequency += int(frequency)
    
    beforeAdd = len(seenFrequencies)
    seenFrequencies.add(currentFrequency)
    afterAdd = len(seenFrequencies)

    if beforeAdd == afterAdd:
        print("Frequency: {}".format(currentFrequency))
        break
