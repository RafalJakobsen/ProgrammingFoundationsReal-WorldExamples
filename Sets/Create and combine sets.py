# Creating and Combining SEts of Friends

college = set(["Bill", "Katy", "Verne", "Dillon",
               "Bruce", "Olivia", "Richard", "Jim"])

coworker = set(["Aaron", "Bill", "Brandon", "David",
                "Frank", "Connie", "Kyle", "Olivia"])

family = set(["Garry", "Landon", "Larry", "Mark",
              "Olivia", "Katy", "Rae", "Tom"])

print(college)
print(len(college))
print(len(coworker))
print(len(family))

friends = college.union(coworker, family)
print(friends)
print(len(friends))
