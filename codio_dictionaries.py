'''
Machew Kp
Dictionaries From Codio
(Slight Work)
'''
'''
Are mutable - the contents of the data structure can change
Are dynamic - the size of the data structure can grow or shrink
Can be nested - elements in the data structure can be other lists or dictionaries
Lists use an index to access an element
Dictionaries use a key to access a value
'''
person = {'name' : 'Amy', 'age' : 32, 'occupation' : 'software engineer'}
print(person['occupation'])
numbers = dict([(0, 'zero'), (1, 'one'), ('2', 'two')])
print(numbers)
capitals = dict([
  ('Canada', 'Ottawa'),
  ('France', 'Paris'),
  ('New Zealand', 'Wellington'),
  ('Argentina', 'Buenos Aires')
])

print(capitals)
'''
Iterating Over a Dictionary
To better understand the built-in capabilities of dictionaries, use the dir() method and pass it an empty dictionary. This method returns all of the methods and attributes associated with a dictionary.
'''
print(dir({}))
print("You should see the __iter__ method. This means you can iterate over a dictionary with a for loop.")
# Example Of Iterating Over A Dictionary:
print("Example Of Iterating Over A Dictionary: ")
hero = {
  'name' : 'Moira',
  'role' : 'support',
  'health' : 200
}

for item in hero:
  print(item)
print()
print()
my_dict = {
  'name' : 'Moira',
  'role' : 'support',
  'health' : 200
}
for i in my_dict.items():
  key = i[0]
  value = i[1]

teams = {
  'Houston' : 'Heat',
  'Oregon' : 'Ravens',
  'Atlanta' : 'Phoenix'
}
'''
Select all of the ways which would produce the dictionary:
    Heat
    Ravens
    Phoenix
'''
for values in teams.values():
    print(values)
for key in teams:
    print(f'Key: {key}, Value: {teams[key]}')

# The get() Method: Python includes the get() method which takes a key as a parameter and returns the associated value.
print("Example Of The Get Method: ")
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print(watches.get('Tank'))
print(f'{watches.get("Submariner")}')
print()
print()
dict1 = {
  'red' : 'english',
  'rouge' : 'french',
  'rojo' : 'spanish'
}

dict2 = {
  'blue' : 'english',
  'bleu' : 'french',
  'azul' : 'spanish'
}
dict1.update(dict2)
print(dict1)
print()
print(dict2)
my_dict1 = {
  'first' : '1st',
  'second' : '2nd',
  'third' : '3rd',
  'fourth' : '4th'
}
print(len(my_dict1))
print('\nNested Dictionaries: ')
actor = {
  'first_name' : 'Denzel',
  'last_name' : 'Washington',
  'films' : {
    'Malcolm X' : 1992,
    'The Hurricane' : 1999,
    'Training Day' : 2001,
    'Fences' : 2016
  }
}
arist = {"First Name": "LUCKI",
         "Last Name": "Second Coming Of Christ",
         "Top 3": {1:"3D Outro",2:"GOODFELLAS",3:"Nigo"}}
artists = {"Lucki":{"3D Outro, GoodFellas","All love"},
           "Baby Smoove":{"DX","I Dare you","Freestyle"},
           "Yeat":{"Double","Demon Tiez","Better Off"}}
actor2 = {
  'first_name' : 'Denzel',
  'last_name' : 'Washington',
  'films' : [
    ('Malcolm X', 1992),
    ('The Hurricane',  1999),
    ('Training Day', 2001),
    ('Fences', 2016)
  ],
  'oscars' : [{
    'award' : 'Best actor in a supporting role',
    'film' : 'Glory',
    'year' : 1990
  }, {
    'award' : 'Best actor in a leading role',
    'film' : 'Training Day',
    'year' : 2002
  }]
}

print(actor)
print(f'Example 1: \n\t{actor}')
print(f'Example 2: \n\t{arist}')
print(f'Example 3:   \n\t{artists}')
print(f"Example 4: \n\t{actor2}")
# Pretty Printing: Python has a pretty print module (called pprint) that helps when printing things like nested dictionaries.
# Start by importing pprint.
import pprint
# Then replace the print statement with pprint.pprint(actor).
  #  Python will automatically indent and provide line breaks so that the data is much easier to read and understand
pprint.pprint("Example 5 Using The Pretty Print Package: \n\t " + artists)
# Notice that pprint automatically sorts the dictionary by keys.
