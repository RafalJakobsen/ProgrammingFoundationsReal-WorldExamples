row = ["Ford", "Audi", "BMW", "Lexus"]
row.append("Mercedes")
print(row)
print(row[4])
row[2] = "Jeep"
print(row)
print(row[2])
row.append("Honda")
print(row)
print(row[4])
row.insert(0, "Kia")
print(row)
print(row[4])
print(row.index("Mercedes"))
print(row.pop(5))
print(row)
row.remove("Lexus")
print(row)
