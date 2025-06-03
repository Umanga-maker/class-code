a = [1, 2, 3, 4]
b = ['a', 'b', 'c']

for idx in range (len(a)):
    print(a[idx], b[idx])

# Use zip
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']

for val1, val2 in zip(a, b):# to see an error, use argument 'strict=True'
    print(val1, val2)