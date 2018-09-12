# Sorting Friends into Sets

# set of all friends
friends = set(["Mark", "Rae", "Verne", "Richard",
               "Aaron", "David", "Bruce", "Garry",
               "Bill", "Connie", "Larry", "Jim",
               "Landon", "Dillon", "Frank", "Tom",
               "Kyle", "Katy", "Olivia", "Brandon"])

# set of people who live in my zip code
zipcode = set(["Jerry", "Elaine", "Cindy", "Verne",
               "Rudolph", "Bill", "Olivia", "Jim",
               "Lindsay", "Rae", "Mark", "Kramer",
               "Landon", "Newman", "George"])

# set of people who play Munchkin
munchkins = set(["Steve", "Jackson", "Frank", "Bill",
                 "Mark", "Landon", "Rea"])

# set of Olivia`s friends
olivia = set(["Jim", "Amanda", "Verne", "Nestor"])

local = friends.intersection(zipcode)
print(local)
invite = local.difference(local)
print(invite)
invite = invite.symmetric_difference_update(olivia)
print(invite)
