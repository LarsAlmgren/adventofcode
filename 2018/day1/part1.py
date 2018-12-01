frequencies = [line.rstrip('\n') for line in open('data1.txt')]

print("Frequency: {}".format(sum(int(freq) for freq in frequencies)))
