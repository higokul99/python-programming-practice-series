"""
Given a string, count how many times each character appears.

Input : "banana"

Output : 
{
'b' : 1,
'a' : 3,
'n' : 2
}

"""

def count_freq(input_str):
    freq_dict = {}
    for ch in input_str:
        if ch in freq_dict:
            freq_dict[ch] += 1
        else:
            freq_dict[ch] = 1

    return freq_dict

def cleaner_count_freq_approach(input_str):
    freq_dict = {}
    for ch in input_str:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1 

    return freq_dict

def most_frequent(input_str_dict):
    

input_str = "banana"
print(count_freq(input_str))