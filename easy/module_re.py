import re

pattern = "was"
text = "This was a was mistake"

match = re.findall(pattern, text)
print(match)


print("==============")

#Removing all white space
my_string1 = "C O D E"
whitespace = re.compile(r'\S+')
#result = re.sub(my_string,whitespace)


ms2 = "This is 55 Rs"
count = re.findall(r'\d', ms2)
print(len(count))

no_of_char = re.findall(r'[A-Z]',ms2)
print(no_of_char)
print(len(no_of_char))
