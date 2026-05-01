def is_palindrome_two_pointer(text):
    """
    Approach 3
    Check palindrome using two-pointer technique.
    More memory efficient for large strings.
    """
    # Clean the string first
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
print(is_palindrome_two_pointer("madam"))          # True
print(is_palindrome_two_pointer("hello"))          # False
print(is_palindrome_two_pointer("No 'x' in Nixon")) # True