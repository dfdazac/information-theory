from collections import Counter, defaultdict
import math
import re

## parse input file, convert to lowercase, remove punctuation
f = open("../data/Jack.txt")
data = f.read().lower()
regex = re.compile('[^a-z ]')
data = regex.sub('', data)

def get_ngram_probs(data, n):
    # Count ngrams
    ngram_counts = Counter([data[i:i + n] for i in range(len(data) - 1)])
    total = sum(ngram_counts.values())
    # Compute ngram probabilities
    probabilities = dict()
    for ngram in ngram_counts:
        print("'" + ngram + "': ", ngram_counts[ngram])
        probability = ngram_counts[ngram]/total
        probabilities[ngram] = probability

    return probabilities

uni_probs = get_ngram_probs(data, 1)
bi_probs = get_ngram_probs(data, 2)

# Compute cross entropy H_c(P_XY, P_X P_Y)
cross_entropy = 0
for pair in bi_probs:
    first, second = (pair[0], pair[1])
    cross_entropy -= bi_probs[pair] * math.log2(uni_probs[first] * uni_probs[second])

print(f'The cross entropy is {cross_entropy:.4f}')
