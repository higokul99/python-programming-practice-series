from collections import Counter

def check_anagram(list_a: list, list_b: list) -> list :
    if len(list_a) != len(list_b):
        return False

    return Counter(list_a) == Counter(list_b)


def check_anagram_2(list_a: list, list_b: list) -> list :
    if len(list_a) != len(list_b):
        return False

    return sorted(list_a) == sorted(list_b)

list_a = ['a','b','c','f','d','f']
list_b = ['a','b','c','d','f','f']
print("1 :",check_anagram(list_a, list_b))
print("2 :",check_anagram_2(list_a, list_b))