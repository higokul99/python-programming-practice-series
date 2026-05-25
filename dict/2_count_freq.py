def count_frequency(input):
    input = input.strip()
    char = {}

    for ch in input:
        if char.get(ch):
            char[ch] += 1
        else:
            char[ch] = 1
        
    return char


input = "banana"
print(count_frequency(input))