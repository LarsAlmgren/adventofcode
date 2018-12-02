boxes = [line.rstrip('\n') for line in open('data1.txt')]

def getSubsets(box):
    theSet = set()
    for i in range(0, len(box)):
        theSet.add(box[0:i] + box[i+1:len(box)])
    return theSet

allSubsets = set()
for box in boxes:
    subsets = getSubsets(box)
    for possible in subsets:
        if possible in allSubsets:
            print("Duplicate: " + possible)
            break
        allSubsets.add(possible)

