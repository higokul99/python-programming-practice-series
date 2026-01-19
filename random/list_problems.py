
text = "apple"
count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1


print(count)


text = "apple"
count = {} # to store occurence of char
index = {} # to store index of each char

for i,char in enumerate(text):
    if char in count:
        count[char] += 1
        index[char].append(i)
    else:
        count[char] = 1
        index[char] = [i]

print(f"Counts: {count}")
print(f"Indices: {index}")


text2 = "banana"
count2 = {}
index2 = {}

for i,char2 in enumerate(text2):
    if char2 in count2:
        count2[char2] += 1
        index2[char2].append(i)
    else:
        count2[char2] = 1
        index2[char2] = [i]

print(f"Counts: {count2}")
print(f"Indices: {index2}")


"""
Imagine you are building a simple inventory system for a fruit stand.

Your Task:

Create a dictionary called prices.

Map "apple" to 0.50 and "banana" to 0.30.

If a customer buys 3 apples and 2 bananas, use your dictionary to calculate the total cost.

Try to write the code for that
"""

prices = {
    "apple" : 0.50,
    "banana" : 0.30
}

apple = 3
banana = 2

price_of_apple = prices.get("apple")
print(price_of_apple)
price_of_banana = prices.get("banana")
total = (apple*price_of_apple ) + (banana*price_of_banana)
print(total)


loginids = [10,22,10,35,22,10]
id_to_name = {10:"Devin",22:"Alex",35:"Sasha"}

login_counter = {}

for userid in loginids:
    name = id_to_name[userid]
    login_counter[name] = login_counter.get(name,0)+1

print(login_counter)


thename = "Hrishikesh"
char_counter = {}
char_index = {}
for i,char in enumerate(thename.lower()):
    print(f"{i}{char}")
    char_counter[char] = char_counter.get(char,0)+1
    if char in char_index:
        char_index[char].append(i)
    else:
        char_index[char] = [i]

print(char_counter)
print(char_index)
max_char = max(char_counter, key=char_counter.get)
print(max_char)
print("index:",char_index[max_char])
