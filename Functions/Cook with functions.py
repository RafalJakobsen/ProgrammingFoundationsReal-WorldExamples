# A Functional Breakfast

cheese = "cheddar"


def mix_and_cook():
    print("Mixing the ingredients")
    print("Greasing the frying pan")
    print("Pouring the mixture into a frying pan")
    print("Cooking the first side")
    print("Flipping it!")
    print("Cooking the other side")


def make_omelette(ingredient):
    mix_and_cook()
    omelette = "a {} omelette".format(ingredient)
    return omelette


def make_pancake():
    global cheese
    cheese = "swiss"
    mix_and_cook()
    pancake = "a {} pancake".format(cheese)
    return pancake


print(make_omelette("bacon"))


def fancy_omelette(*ingredients):
    mix_and_cook()
    omelette = "a fancy omelette with {} ingredients".format(len(ingredients))
    return omelette


print(fancy_omelette("sausage", "onion", "pepper", "pianch", "mushroom"))
print(make_pancake())
