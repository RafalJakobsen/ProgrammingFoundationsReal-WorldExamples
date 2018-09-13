# Loading the dishwasher

# dirty dishes in the sink
sink = ["bowl", "plate", "cup"]

for dish in list(sink):
    print("Putting {} in the dishwasher".format(dish))

print(sink)

for dish in list(sink):
    print("Putting {} in the dishwasher".format(dish))
    sink.remove(dish)

print(sink)
