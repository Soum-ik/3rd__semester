# polymorphisum and inheritance
class Animal: 
    def __init__(self, name):
        self.name = name;
        print(self.name + "was addopted!");

    def run(self):
        print("runnings!");

class Dog(Animal):
    def dack(self):   
        print ("woolf!");
       
newObj = Dog("sadik");
newObj.dack();
