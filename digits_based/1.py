"""
Print the last digit of a number.
"""
n = 456
last_digit = n % 10
print(last_digit)

"""
Remove the last digit from a number
"""
n2 = 456
remaining = n2 // 10
print(remaining)


"""
Print last digit and remaining number
"""

n3 = 456
last_digit = n3 % 10
remaining = n3 // 10
print(last_digit, remaining)


"""
Extract all digits
"""
n4 = 456
while n4 > 0:
    last_digit = n4 % 10
    print(last_digit)
    n4 = n4 // 10

"""
Count digits.
"""
n = 45678
count = 0
while n > 0:
    count += 1
    n = n // 10

print("Count:",count)


"""
Sum of Digits
"""
n = 456
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

print("Sum:", sum)


"""
Product of digits
"""
n = 234
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n = n // 10

print("Product:",product)


"""
Reverse a Number
"""
n = 12345
reverse = 0
while n > 0:
    d = n % 10
    reverse = reverse * 10 + d
    n = n // 10

print(reverse)