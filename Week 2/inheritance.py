class GrandParent:
    def printGrandParent(self):
        print("I am grand parent")
class Parent(GrandParent):
    def printParent(self):
        print("I am parent")
class Child(Parent):
    def printChild(self):
        print("I am child")

c1 = Child()
g1 = GrandParent()
p1 = Parent()

c1.printChild()
c1.printParent()
c1.printGrandParent()
g1.printGrandParent()
p1.printGrandParent()
p1.printParent()