class Dog: 
    def __init__(self, name):
        self.name = name;
        print(self.name + 'was is king');
    
    def bark(self):
        print('woolf');

spot = Dog("lion")
spot.bark();
