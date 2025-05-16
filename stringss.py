# Create a list of strings
w = ["do", "on","banana", "at", "apple", "tree"]

# Remove strings with length less than 3
filtered_words = [word for word in w if len(word) >= 3]

print(filtered_words)