# A Garage Full of Classy Vehicles

class Vehicle:  # Base Bechicle class
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4  # a full tank of gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print("The {} {} goes VROOM!".format(self.color, self, manuf))
        else:
            print("The {} {} sputters out of gas".format(self.color, self.manuf))


class Car(Vehicle):  # Inherits from vehicle class
    # turn the radio on
    def radio(self):
        print("Rockin` Tunes!")

    # open the window
    def window(self):
        print("Ahhh... fresh air!")


class Motorcycle(Vehicle):  # Inherits from Vehicle class
    # put on motocycle helmet
    def helmet(self):
        print("Nice and safe!")


# run shell
my_car = Car("red", "Mercedes")
my_mc = Motorcycle("silver", "Harley")

print(my_car.drive)

class ECar(Car):  # Inherits from Car class

    # an eco-friendly drive method
    def drive(self):
        print('The {} {} goes ssshhhhh!'.format(self.color, self.manuf))


# create and use an electric car
my_ecar = ECar('white', 'Nissan')
my_ecar.window()
my_ecar.radio()
my_ecar.drive()

# access the lingering gas tank
print(my_ecar.gas)
