# Create Class Car with 1 Constructor and 3 Methods
class Car():
    # Constructor with at least 4 properties
    def __init__(self, make, model, color, horsepower, maxspeed):
        self.make = make
        self.model = model
        self.color = color
        self.horsepower = horsepower
        self.maxspeed = maxspeed

    # 3 Methods - 1 drive with "speed" parameter
    def drive(self, speed):
        if (speed <= self.maxspeed):
            print(self.make + " " + self.model + " is driving at a speed of " + str(speed) + "km/h with a max speed of " + str(self.maxspeed) + " km/h.")
        else:
            print("Ouch... " + self.make + " " + self.model + " with a max speed of " + str(self.maxspeed)  + " km/h is driving " + str(speed) + " km/h.")

    def drive_backwards(self):
        print(self.make + " " + self.model + " reverses slowly.")

    def stop(self):
        print(self.make + " " + self.model + " stopped.")

# Create Objects with properties
bmw_m8 = Car("BMW", "M8", "White", 625, 305)
audi_tt = Car("Audi", "TT", "Black", 200, 250)
opel_mokka = Car("Opel", "Mokka", "Blue", 136, 208)

# Call the methods
#print(audi_tt.maxspeed) #For testing
audi_tt.drive(250)
opel_mokka.stop()
bmw_m8.drive_backwards()
