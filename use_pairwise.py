data = 'ABCDEFG'
for i in range(len(data)-1):
    print(data[i], data[i+1])

print()

#Using pairwise
from itertools import pairwise
for pair in pairwise('ABCDEFG'):
    print(pair[0], pair[1])