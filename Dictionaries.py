# Matthew Kilaptrick
# 2-29-24
# Dictioaries
#It is best to think of a dictionary as a set of key: value pairs, with the
#requirement that the keys are unique (within one dictionary).
#A pair of braces creates an empty dictionary: {}. Placing a comma-separated list
#of key: value pairs within the braces adds initial key:value
#pairs to the dictionary. This is also the way dictionaries are written on output
import pygame
import random
import tabulate
#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================
# PRIME NUMBERS
print("Prime Numbers: ")
print("Example From Youtube: ")
print("#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================")
def raven():
    primes = []
    limit = 100
    for x in range(2+limit+1):
        isprime = True
        for divisor in range(2, x):
            if(x % divisor == 0):
                isprime = False
                break
        if isprime:
            primes.append(x)
    print("List of prime numbers: ")
    print(primes)
    print()
    print("Vertical Print: ")
    # Writing to the file:
    # Open the file:
    file = open('../PrimeNumbers.txt', 'w')
    index = int(0) # ☚☚☚☚☚☚☚☚ index
    for primeNums in primes:
        print(f'{index+1}. {primeNums}')
        file.write(f'{index+1}. {primeNums}\n')
        index+=1
    file.close()
if __name__== '__main__':
    raven()
print("#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================")
#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================#========================
tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
tel['irv'] = 41127
print("After Adding New Elements to the dictionary:")
print(tel)

# prints a set of all the keys
for key in tel.keys():
    print(key)

# prints key value pairs
for key in tel.keys():
    print(key, tel[key])

# prints a list of all of the values
for value in tel.values():
    print(value)
#ets
#A set is an unordered collection with no duplicate elements. Sets support mathematical operations like union, intersection, difference, and symmetric difference.
#Creating a Set
#Curly braces or the set() function can be used to create sets. To create an empty set you have to use set(), not {}.
#Here is a brief demonstration:
print("Example of a set: ")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
if 'orange' in basket:
    print(True)
print()# Space:
print("After Adding An Element To The Set: ")
basket.add('pineapple')
print(basket)
# Comparing Sets: There are a number of operators that llow you to compare them mebers of different sets:
print("Comparing Sets: There are a number of operators that llow you to compare them mebers of different sets:")
a = set('abracadabra')
b = set('alacazam')
a - b # letters in a but not in b
print(basket)
#P------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------------")
suits = ['coin', 'string', 'myriad']
suits.pop()
suits.remove('string')
suits.append('cup')
print(suits)
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']
print(suits)

prime_list = [x for x in range(10, 11) for y in range(2,x) if x % x == 0 and x % 1 == 0 and x % y != 0]
print(prime_list)

myset = set([])
second_set = set([])
for names in range(6):
    names = str(input("Enter names: "))
    myset.add(names)
print(myset)
print()
for names in range(7):
    names = str(input("Enter more names into the new set: "))
    second_set.add(names)
print(second_set)

print("The same name in both list using intersection: ")
for names in myset.intersection(second_set):
    print(names)
print()
print("The following names either in set 1 or set 2:")
for names in myset.union(second_set):
    print(names)

print()
print("The diffence: ")
for names in myset.difference(second_set):
    print(names)

#=================#=================#=================#=================#=================#=================
# Removing duplicates :
'''
remove_duplicate
Given a string like “hello world”, write a function remove_duplicate() 
that returns unique words (i.e. must not contain duplicate words). 
Starter code has been provided to ask the user for input, call your function, 
and print out what is returned so you can test it.
'''
def remove_duplicate(userInput):
    words = userInput.split()
    hsh = set()
    for word in words:
        if word not in hsh:
            # print(word, end=" ")
            hsh.add(word)
    return hsh


##starter code - do not edit
user_input = input()  ## get user input
unique_words = remove_duplicate(user_input)  ## call function with user input
print(sorted(unique_words))  ## print what was returned from function








