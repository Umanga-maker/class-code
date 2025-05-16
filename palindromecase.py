def is_palindrome(s):
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Take input from the user
user_input = input("Enter a string: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print("✅ The string is a palindrome.")
else:
    print("❌ The string is not a palindrome.")