def add(n):
    return n + n

numbers = [2,3,4]

result = map(add,numbers)
print(list(result))