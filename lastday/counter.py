"""
Find first char with frequency = 1
"""
from collections import Counter


s = "aabbcde"
count = Counter(s)

for ch in s:
    if count[ch] == 1:
        print(ch)
