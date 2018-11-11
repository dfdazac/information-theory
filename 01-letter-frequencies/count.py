import string
from collections import Counter

# Read data
with open('../data/Jack.txt') as file:
    data = file.read().lower()

# Remove punctuation
alphabet = set(string.ascii_lowercase)
letters = ''
for letter in data:
    if letter in alphabet:
        letters += letter

# Count letters
counts = Counter(letters)
most_common = counts.most_common(1)[0]
print('Most common letter is {} with {:d} occurrences'.format(most_common[0],
                                                              most_common[1]))
