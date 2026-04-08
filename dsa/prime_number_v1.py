"""
Write a function that takes a range of integer as input and 
determines whether it is a prime number.
"""
def is_prime(num):
    """
    Return True if n is a prime number.
    Else return False.
    """
    if num == 1:
        return False
    
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(1,200001):
        print(f"{i} is {"a Prime" if is_prime(i) else "not a prime"}")
