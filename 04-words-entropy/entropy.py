from collections import Counter
import math
import re

## parse input file, convert to lowercase, remove punctuation
f = open("../data/Jack.txt")
data = f.read().lower()
regex = re.compile('[^a-z ]')
data = regex.sub('', data)

# Collect list of words by splitting with space
words = data.split()
word_counts = Counter(words)
total = sum(word_counts.values())

entropy = 0
for word in word_counts:
    print(f'{word}: {word_counts[word]}')
    probability = word_counts[word]/total
    entropy -= probability * math.log2(probability)

print(f'Total: {total:d}')
print(f'The entropy is {entropy:.4f}')
print(word_counts.most_common(10))
