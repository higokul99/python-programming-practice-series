# Problem : Check if given number is prime

def is_prime(n):
    if n <= 1:
        return print(f'{n} is not a prime number')

    for i in range(2,n-1):
        if n % i ==  0:
            return print(f'{n} is not a prime number')

    return print(f'{n} is a prime number')

is_prime(1)
is_prime(2)
is_prime(3)
is_prime(6)
is_prime(0)
is_prime(17)