class A:
    def hablar(self):
        print("Hola desde A")

class F(A):
    def hablar(self):
        print("Hola desde F")
       

class B(A):
    pass

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    pass


d = D()

d.hablar()