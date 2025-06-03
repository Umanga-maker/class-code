# Don't use loops at all
numbers = [12, 45, 54, 67, 58, 73]
result = 0
for num in numbers:
    result += num

print(result)

# Instead using for loop we can use built in sum method
result = sum(numbers)
print(result)