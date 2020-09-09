# Implicit Inheritance

class Parent(object):

    def implicit(self):
        print("PARENT IMPLICIT()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#pass let's python know that you're expecting an empty block.
