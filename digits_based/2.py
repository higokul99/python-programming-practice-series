"""
Check whether the given number is palindrome number or not?
"""

n = 121
og = n
reverse = 0
while n > 0:
    d = n % 10
    reverse = reverse * 10 + d
    n = n // 10

print("Number : ", og)
print("Reverse :",reverse)
if og == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")