# Create Class Dog with Constructor and Methods
class Dog:
    def __init__(self, name, color, breed, height, weight):
        self.name = name
        self.color = color
        self.breed = breed
        self.height = height
        self.weight = weight

    def fly(self):
        print(self.name + ", the " + self.color + " dog, is flying")
    
    def bark(self, bark_type):
        print(self.name + " barks " + bark_type)


# Create Object "Charlie" and "Lisa" from Class Dog
charlie = Dog("Charlie", "Black and White", "Dalmatian", 0.8, 15)
lisa = Dog("Lisa", "Brown", "Terrier", 0.25, 1.5)

#print(charlie.name) #For testing
#print(lisa.weight) #For testing

# Add method to "Charlie" without parameter
charlie.fly()

# Add method to "Lisa" with parameter
lisa.bark("angrily")
