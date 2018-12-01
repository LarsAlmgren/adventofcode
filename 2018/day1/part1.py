frequencies = [line.rstrip('\n') for line in open('data1.txt')]

currentFrequency = 0

print("Frequency: {}".format(sum(int(freq) for freq in frequencies)))

