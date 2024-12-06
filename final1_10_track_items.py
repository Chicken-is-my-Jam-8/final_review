inventory = {"apple":10,
             "banana":5,
             "orange":8}
sold_items = ["apple", "banana", "grape", "apple", "orange", "banana"]
num = 0
print(inventory)
for x in sold_items:
    in_inventory = True
    try:
        s = inventory[x]
    except KeyError:
        in_inventory = False
    if in_inventory == True:
        num = inventory[x]
        num -= 1
        inventory[x] = num
    elif in_inventory == False:
        inventory[x] = 0
        num = inventory[x]
        num -= 1
        inventory[x] = num
print(inventory)
