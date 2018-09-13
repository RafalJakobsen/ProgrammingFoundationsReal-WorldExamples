# Ordering a Pizza that Verne Can Eat

# things that Verne does not eat
diet_restrictions = set(["meat", "cheese"])

# decide which pizza to order
if "meat" and "cheese" in diet_restrictions:
    print("Get a vegan pizza.")

elif "meat" in diet_restrictions:
    print("Get a cheese pizza")

else:
    print("Get something else.")

# I`ll have the special!

today = "Saturday"

if today is "Sunday":
    print("Order the spinach pizza")
elif today is "Monday":
    print("Order the mushroom pizza")
elif today is "Tuesday":
    print("Order the pepperoni pizza")
elif today is "Wednesday":
    print("Order the chicken pizza")
elif today is "Thursday":
    print("Order the veggie pizza")
elif today is "Friday":
    print("Order the sausage pizza")
elif today is "Saturday":
    print("Order the Hawaiian pizza")
