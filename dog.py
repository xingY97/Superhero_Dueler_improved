class Dog:
    #Required properties are defined inside the __init__ constructor method
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    #Method are defined as their own named functions inside the class
    #Remember to put the 'self' parameter everytime we make a class method

    def bark(self):
        print('Woof!')

# instantiation call that creates a Dog object:

