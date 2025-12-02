my_list = [22,3,55,67,12,26,78,56,6,2,43]
print("My List is :",my_list)

min_value = my_list[0]
for item in my_list:
    if min_value > item:
        min_value = item

print("Minimum value in the list is ",min_value)