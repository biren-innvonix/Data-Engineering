class Demo:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print("Your name is: ",self.name)

dog_name = input("Enter your name: ")
d1 = Demo(dog_name)
d1.print_name()