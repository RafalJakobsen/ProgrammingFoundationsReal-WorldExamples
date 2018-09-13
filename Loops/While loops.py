# Scrubbing a stuborn pan

import random

dirty = True  # state of the pan
scrub_count = 0  # numbers of scrubs

while (dirty):
    scrub_count += 1
    print("Scrub the pan: {}".format(scrub_count))

    print("Rinse & check if the pan is clean.")

    if not random.randint(0, 9):
        print("All clean!")
        dirty = False
    else:
        print("Still dirty...")

# if you want fixed numbers of try
while (dirty):
    scrub_count += 1
    print("Scrub the pan: {}".format(scrub_count))

    if not random.randint(0, 9):
        print("All clean!")
        dirty = False
    else:
        print("Still dirty...")

    print("Rinse & check if the pan is clean.")
