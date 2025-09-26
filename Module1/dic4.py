inventory = {"bananas": 312, "apples": 430,
             "oranges": 525, "pears": 217}
#A new shipment of bananas arriving 
inventory["bananas"] += 200
print(inventory)

# The order of the k's is not defined, or is it?
for k in inventory.keys():  
   print("Got key", k, "which maps to value", inventory[k])

# deep copy vs shallow copy
#shallow_list = inventory.keys()
ks = list(inventory.keys()) #deep copy, using list construcotr
l2 =inventory.keys() #shallow copy
print(ks)

inventory["strawburries"] = 500
print(inventory)
print(ks)
print(l2)

