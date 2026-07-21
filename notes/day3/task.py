class A:
    def greet(self):
        print("hello from class a")

class B(A):
    def greet(self):
        print("hello from class b")

class C(A):
    pass

class D(B,C):
    pass

d=D()
d.greet()


# output: hello from class b  
"""this is because of the method resolution order (MRO) 
 in Python, which follows the C3 linearization algorithm. In this case, when 
 we call d.greet(), Python looks for the greet method in class D first, then
in class B, and finds it there before checking class C or A."""