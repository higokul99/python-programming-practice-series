# Create a list of fruits and access elements
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

#Basic operations
print(fruits[0])
print(fruits[-1])
print(fruits[1:4])
print(len(fruits))


middle = len(fruits)//2
print(fruits[middle])


# List Methods
numbers = [ 1, 2, 3]

# adding elements
numbers.append(4)
numbers.insert(0,0)
numbers.extend([5,6])


# Removing elements
numbers.pop() # remove last
numbers.pop(0) # removes the no
numbers.remove(3) # remove first 3 occurance in the list
del numbers[1] # remove the element at index 1

print(numbers)


new_numbers = [numbers,[7,8]]
print(new_numbers)


# Challenge

nums = []
nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)
print(nums)
middle = len(nums) // 2
nums.insert(middle, 50)
nums.pop()
print(nums)


# Search and sort
colors = ["red", "blue", "green", "red", "yellow"]

#searching
print(colors.index("green")) # index 2
print(colors.count("red")) # 2
print("blue" in colors) # True

#sorting
colors.sort() # sorts alphabetical
colors.sort(reverse=True) # reverse alphabetical
colors.reverse() # reverse order

# safe sorting (original unchanged)
sorted_colors = sorted(colors)


# Find all indices of a repeated element in a list
print("Find all indices of a repeated element in a list")
print(colors)
for idx, color in enumerate(colors):
    if colors.count(color) > 1:
        print(f"COLOR: {color} , INDEX: {idx}")


# List comprehension

squares = [i**2 for i in range(2,5,1)]
print(squares)

even_squares = [i**2 for i in range(10) if i % 2 == 0]

labels = ["even" if i % 2 == 0 else "odd" for i in range(5)]
print(labels)


list1 = [1,2,3,4]
list2 = [4,5,6]

combined = list1 + list2
repeated = list1 * 3
print(combined)
print(repeated)


list3 = list1 # Shallow copy - Object is same
list4 = list1.copy()
list5 = list1[:] 

list6 = list1 + list2
list6 = list(set(list6))
# for a in list1:
#     for b in list2:
#         if a != b:
#             list6.append(a)

print(list6)