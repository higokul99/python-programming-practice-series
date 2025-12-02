my_string = "Malayalam"
rev_string = my_string[::-1]

if my_string.lower() == rev_string.lower():
    print(f"{my_string} is a Palindrome")
else:
    print("Not Palindrome")
