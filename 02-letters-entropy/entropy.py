import math
import re

## parse input file, convert to lowercase, remove punctuation
f = open("../data/Jack.txt")
data = f.read().lower()
regex = re.compile('[^a-z ]')
data = regex.sub('', data)

## create a dictionary containing the frequencies for all characters (incl. space)
alphabet = "abcdefghijklmnopqrstuvwxyz "
frequencies = {c: data.count(c) for c in alphabet}
total = sum(frequencies.values())

entropy = 0
for c in alphabet:
    print("'" + c + "': ", frequencies[c])
    probability = frequencies[c]/total
    entropy -= probability * math.log2(probability)

print(f'Total: {total:d}')
print(f'The entropy is {entropy:.4f}')
