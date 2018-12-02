from sets import Set

boxes = [line.rstrip('\n') for line in open('data1.txt')]

def getDistinctLetters(box):
    letters = set()
    for letter in box:
        letters.add(letter)
    return letters

twos = 0
threes = 0

for box in boxes:
    gotTwo = False
    gotThree = False
    distinctLetters = getDistinctLetters(box)
    for letter in distinctLetters:
        theCount = box.count(letter)
        if gotTwo and gotThree:
            break
        if not gotTwo and theCount == 2:
            twos += 1
            gotTwo = True
        if not gotThree and theCount == 3:
            threes += 1
            gotThree = True

print("Twos: " + str(twos))
print("Threes: " + str(threes))
print("Checksum: " + str(twos * threes))
