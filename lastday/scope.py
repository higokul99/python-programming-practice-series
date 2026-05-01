def func1():
    x = 100

def func2():
    print(x)


global_scope = 10

def func0():
    print(global_scope)

func0()
func2()
func1()
