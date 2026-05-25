class A:
    def show(self):
        print("Show method of A class")

class B(A):
    def show(self):
        super().show()
        print("Show method of B class")

class C(A):
    pass

class D(B,C):
    def show(self):
        super().show()
        print("Show method of D class")

b = B()
b.show()

d = D()
d.show()
print(D.mro())


print(isinstance(b, A))
print(issubclass(D,A))