list_a = ["a", "b", "c", "d", "e", "f", "g", "h"]
list_b = ["a", "b", "c", "d", "e", "f", "g", "h"]

new_list = list_a + list_b
print(new_list)

list_a.extend(list_b)
print(list_a)