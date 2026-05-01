tup1 = (1,"a", True)
tup2 = ( 4,5,6 )

print( tup1 + tup2 )

dict1 = { "a": 1, "b": 2 }
dict2 = { "b": 3, "d": 4 }

print(dict1 | dict2)

result_dict = {}

for key in dict1:
    result_dict[key] = dict1[key]

for key in dict2:
    if key in result_dict:
        result_dict[key] +=  dict2[key]
    else:
        result_dict[key] = dict2[key]

print(result_dict)