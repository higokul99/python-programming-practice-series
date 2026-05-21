import re

text = "abbbb abbbbbbb abbb abbbbbbbb aabbbbb"

# pattern : 'a' followed by 4 to 8 b's
pattern = r"a(b{4,8})"

matches = re.findall(pattern, text)
print(matches)