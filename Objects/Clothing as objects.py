# The Blueprints for Jeans

class jeans:

    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print("Putting on {}x{} {} jeans".format(self.waist, self.length, self.color))
        self.wearing = True

    def take_off(self):
        print("Taking off {}x{} {} jeans".format(self.waist, self.length, self.color))
        self.wearing = False

my_jeans = jeans(31,32,"blue")
dir(my_jeans)
my_jeans.put_on()
my_jeans.wearing

class shirt:
    def __int__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

# input on shell
# red = shirt()
# crimson = red
# print(crimson.clean)
# print(red.make_dirty())
# print(red.clean)
# print(crimson.clean)



