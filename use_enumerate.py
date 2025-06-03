numbers = [10, 20, 33, 40]
for idx in range(len(numbers)):
    print(idx, numbers[idx])

# Use enumerate when you need both index and value
numbers = [10, 20, 33, 40]
for idx, val in enumerate(numbers, start = 1):
    print(idx, val)