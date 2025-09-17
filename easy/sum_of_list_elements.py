def sum_list(mylist):
    total = 0
    if not mylist:  # More Pythonic way to check for an empty list
        print("List is empty")
        return 0  # It's good practice to return a value even for an empty list
    else:
        for number in mylist:  # Iterate directly over the elements
            total += number  # More concise way to add
        return total  # Return the sum instead of printing inside the function

# Example usage:
mylist = [2, 200, -2]
result = sum_list(mylist)
print(result)

empty_list = []
result_empty = sum_list(empty_list)
print(result_empty)