'''
Matthew Kilpatrick
Dictionary Work
'''

# Dictonary = A collection of {key:value} pairs orderd and changeable. NO DUPLICATES:
capitals = {"USA": "Washington DC", "India":"New Dehli", "China":"Beijing", "Russia":"Moscow"}
# To get one of the values from a dictionary you get the KEY
print(capitals.get("USA"))
# To UPDATE the dictionary
# This method adds an element into the dictionary
capitals.update({"Germay" : "Berlin"})
# This method updates a current elements already in the dictionary
capitals.update({"USA":"Penis"})
print(capitals)
# To remove an element from the list:
capitals.pop("China")
print(capitals)
# To automatically remove the last element in the dictionary use:
capitals.popitem()
print(capitals)
# To clear the dictionary:
capitals.clear()
print()
#==================================================
# Reupdating the dictionary because we cleared it:
capitals.update({"Machew": "Raven"})
capitals.update({"Lucki":"Tune"})
capitals.update({"Smoove":"babyy"})
capitals.update({"babyface":"race"})
print("Printing The Keys: ")
#=======Important methods:
# To get only the keys from the dictionary: capitals.keys()
keys = capitals.keys()
print(keys)
# USing a for loop to iterate over the keys in the dictionary:
print("Output of the keys but using a for loop ")
index = int(0)
for key in capitals.keys():
    print(f'{index+1}. {key}')
    index+=1
# To get all the VALUES within the dictonary use the .values method
# This methods is basically the opposite of the keys method
print()
print("Output of all the values in the dictionary: ")
values = capitals.values()
print(f'These are the values: {values}.')
print("Using a for loop to iterate over the values: ")
index2 = int(0)
for vals in capitals.values():
    print(f'{index2+1}.{vals}')
    index2+=1
print()
print("Working with the items method: ")
#====== Most important Method: the items method
## returns a dictionary object which resembles a 2d list of tuples
items = capitals.items()
print(items)
print("Using a for loop to list out the keys and the values seperately: ")
print(f'{"Keys"}: {"Values:"}')
for keys, values in capitals.items():
    print(f"{keys}: {values}")

