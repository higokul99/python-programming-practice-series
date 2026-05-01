def is_palindrome(text):
    """
    Check if a string is a palindrome.
    Ignores spaces, punctuation, and case differences.
    """
    # Convert to lowercase and keep only alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                       # False
print(is_palindrome("Was it a car or a cat I saw?"))     # True
print(is_palindrome("12321"))                            # True
print(is_palindrome("hello"))                            # False