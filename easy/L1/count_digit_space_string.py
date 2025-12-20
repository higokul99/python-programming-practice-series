import re

my_string = "Home Address is SMRA 275"

digits_count = 0
for char in my_string:
    if char.isdigit():
        digits_count += 1

def get_no_of_strings():
    x = len(my_string)
    return x

def get_count_words():
    words_list = my_string.split()
    return len(words_list)

count_digits = 

print("Number of digits :",digits_count)
print("Number of whitespaces ",my_string.count(" "))
print("Total string count :",get_no_of_strings())
print("No of words :",get_count_words())
