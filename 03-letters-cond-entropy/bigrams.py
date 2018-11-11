from collections import Counter, defaultdict
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

# count bigrams, map first letter -> {second letter: count}
# We will use this to compute P(second|first)
bigrams = defaultdict(Counter)
for i in range(len(data) - 1):
    first, second = data[i], data[i+1]
    bigrams[first][second] += 1

# Compute unigram probabilities
probabilities = dict()
for c in alphabet:
    print("'" + c + "': ", frequencies[c])
    probability = frequencies[c]/total
    probabilities[c] = probability

# Compute conditional entropy
cond_entropy = 0
for first in alphabet:
    entropy = 0
    bigram_total = sum(bigrams[first].values())
    for second in bigrams[first]:
        conditional_prob = bigrams[first][second]/bigram_total
        entropy -= conditional_prob * math.log2(conditional_prob)

    cond_entropy += probabilities[first] * entropy

print(f'Conditional entropy H(second|first) = {cond_entropy:.3f}')
