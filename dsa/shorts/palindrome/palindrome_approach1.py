def is_palindrome(text):
    """
    Approach 1:

    Check if a string is a palindrome (case-sensitive).
    """
    return text == text[::-1]

# Test cases
print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("madam"))  # True