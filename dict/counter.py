from collections import Counter

words = ['fronx','swift','swift','sierra','xuv700','xuv700','swift']
print(Counter(words))


text = "abracadabra"
text_freq = Counter(text)
print(text_freq)
print(f"Most common : {text_freq.most_common(2)}")


"""
Count vowels (a, e, i, o, u) in a given string, ignoring case.
"""
vowels = "aeiou"
sentence = "Hello world"
filtered_char = ""

# for char in sentence.lower():
#     if char in vowels:
#         filtered_char += char

filtered_char = ''.join(
    char for char in sentence.lower()
    if char in vowels
)

print(Counter(filtered_char))


"""
4. Common Elements Between Lists
Find intersection (shared items) between two lists using Counter union/subtraction.
"""

list1 = [1,2,2,2,3]
list2 = [2,2,3,4]

c1 = Counter(list1)
c2 = Counter(list2)

intersection = c1 & c2
print(f"Intersection: {intersection}")

union = c1 | c2
print(f"Union : {union}")

diff = c1 - c2
print(f"Diff : {diff}")


"""
5. Anagram Check
Verify if two strings are anagrams by comparing character counts.
"""

string1 = "Malayalam"
string2 = "MMalayala"

s1 = Counter(string1.lower())
s2 = Counter(string2.lower())
print(s1,s2)
if s1 == s2:
    print("True")
else:
    print("False")


print(sorted(string1.lower()))