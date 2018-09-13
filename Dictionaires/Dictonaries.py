# A Rolodex Full of Friends

# dictionary of name/number pairs
rolodex = {"Aaron": 5556069,
           "Bill": 5559824,
           "Dad": 5552603,
           "David": 5558331,
           "Dillon": 5552538,
           "Jim": 5555547,
           "Mom": 5552603,
           "Olivia": 5556397,
           "Verne": 5555309}

print(rolodex["Verne"])
print(hash("Verne"))
rolodex["Amanda"] = 5559754
print(rolodex["Amanda"])
print(rolodex["David"])
rolodex["David"] = 5550902
print(rolodex["David"])
rolodex["David"] = (5558331, 5550902)
print(rolodex["David"])
rolodex["David"] = 5558331
rolodex["David (Amanda)"] = 5550902
print(rolodex["David"])
print(rolodex["David (Amanda)"])


def caller_id(lookup_number):
    for name, num in rolodex.items():
        if num == lookup_number:
            return name


print(caller_id(5556397))
print(caller_id(523423324321))
print(caller_id(5552603))
