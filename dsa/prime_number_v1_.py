"""
Write a function that takes a range of integer as input and 
determines whether it is a prime number.
"""
import time

def is_prime(num):
    if num == 1:
        return False
    
    for n in range(2,num):
        if num % n == 0:
            return False
    return True

if __name__ == '__main__':
    start_time = time.time()
    for i in range(1,100001):
        print(f"{i} is {"a Prime" if is_prime(i) else "not a prime"}")
    end_time = time.time()
    print("Time taken to complete :", end_time - start_time)
