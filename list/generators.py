x = [8,3,1]
g = (i**2 for i in x)
print(next(g))

def gen_nums():
    x = [6,3,1]
    for i in x:
        yield i**2

gen = gen_nums()
print(next(gen))