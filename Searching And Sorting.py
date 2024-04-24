import tkinter
from tabulate import tabulate
import random
import pygame
import sympy

'''
Matthew Kilpatrick
4/1/24
Sorting And Searching
'''


def setWork():
    tune = set()
    raven = set
    for x in range(56):
        x = random.randint(1,56)
        tune.update(x)
        raven.update()
    tuneNtrina = tune.union(raven)
    print(tuneNtrina)
setWork()




list = []
for nums in range(23):
    nums = random.randint(1, 200)
    list.append(nums)
print(f'Original List: {list}')
print(f'Reverse List: {sorted(list, reverse=True)}')
newlist = sorted(list)
print(f'New List: {newlist}')
print()
print("Example 2: ")
list2 = []
for nums in range(23):
    nums = random.randint(1, 200)
    list2.append(nums)
print(f'Original List: {list2}')
list2.sort()
print(f'New List: {list2}')
# custom Sorting
words = []
# for word in range(12):
# word = str(input("Enter Random Words 1 - 20:"))
# words.sort(key=len)
# print(words)
# reverse sorting:
# Syntax:
print()


def main():
    list = []
    for num in range(20):
        num = random.randint(1, 45)
        list.append(num)
    list.sort()
    print(list)


if __name__ == '__main__':
    main()


def main2():
    # Sorting a list of dictionaries based on a specific value:
    data = [{'name': 'Machew', 'age': 21}, {'name': 'Raven', 'age': 21}, {'name': 'LUCKI', 'age': 35},
            {'name': 'John', 'age': 20}]
    sorted_data = sorted(data, key=lambda x: x['age'])
    print(sorted_data)


if __name__ == '__main__':
    main2()
print()
print("Example from youtube using the .sort() method: ")


# Example From Youtube:
def youtubeExample():
    print("Example #1:")
    numbers = [3, 56, 234, 27, 8, 5, 23, 12, 11, 345]
    print(f'Original: {numbers}')
    numbers.sort()  # this will put them in ascending order
    print(f'Ascending Order: {numbers}')
    print()
    print("Example 2: With Reverse inside the parameter")
    lucki = []
    for nums in range(13):
        nums = random.randint(1, 78)
        lucki.append(nums)
    print(f'Original List: {lucki}')
    lucki.sort(reverse=True)  # this method will put the list in descending order
    print(f'Reverse style lil nigga: {lucki}')


if __name__ == '__main__':
    youtubeExample()
print()  # spacing
print("Youtube Example To with the sorted() method: ")


def penisEnvy():
    print("Example 3:")
    nums = []
    for lucki in range(23):
        lucki = random.randint(1, 590)
        nums.append(lucki)
    # In addition to the .sort() method, python has a built in sorted() method
    sorted(
        nums)  # unlike the sort method this method will not modify the original list, it will return a new sorted list
    print(f'Original: {nums}')
    print(f'Sorted: {sorted(nums)}')  # Still puts it in ascending order:
    print(f'Reverse: {sorted(nums, reverse=True)}')


if __name__ == '__main__':
    penisEnvy()


# Example 3, what if we a dealing with a list of complex objects:
def listoftuples():
    items = [("Product1", 10),
             ("Product2", 29),
             ("Product3", 30),
             ("Product4", 420)]

    items2 = [("Product1", 45),
              ("Product2", 56),
              ("Product3", 2),
              ("Product4", 12)]

    def sort_item(item):
        return item[1]

    items.sort(key=sort_item)
    print(items)
    # This method does the same thing above but with out the sort_item created function:
    items2.sort(key=lambda item: item[-1])
    print(items2)


listoftuples()
print()


def sort_by_last_char(Strings):
    return sorted(Strings, key=lambda x: x[-1])


def sort_by_first_char(word):
    return sorted(word, key=lambda y: y[+1])


def forloopworked(strings):
    kp = int(0)
    for x in sorted(strings, key=lambda y: y[0]):
        print(f'{kp + 1}. {x}')
        kp += 1
    print()
    print("Printing the same thing but in reverse: ")
    raven = int(0)
    for x in sorted(strings, key=lambda y: y[0], reverse=True):
        print(f'{raven + 1}. {x}')
        raven += 1


print()


def dictionaryWork():
    ListOfStrains = [["Strains", "Indica, Sativa, or Hybrid"], ["Blue Dream", "Hybrid"],
                     ["Pineapple Express", "Hybrid"],
                     ["Sour Tangie", "Sativa"], ["Kushberry", "Indica"], ["Biscotti", "Hybrid"],
                     ["Lavender", "Indica"], ["Alaskan Thunder Fuck", "Hybrid"], ["Bruce Banner", "Hybrid"],
                     ["Jack Herer", "Sativa"]]
    dictionary = {}
    for strain, type in ListOfStrains:
        dictionary.update({strain: type})
    print(dictionary)
    print()
    data2 = [{'strain': 'Blue Dream', 'type': 'Hybrid'}, {'strain': 'Alaskan Thunder Fuck', 'type': 'Hybrid'},
             {'strain': 'Kush-Berry', 'type': 'Indica'}, {'strain': 'Bruce Banner', 'type': 'Hybrid'},
             {'strain': 'Jack Herer', 'type': 'Sativa'}]
    # newstrain = str(input("Enter a new strain to add to the dictionary: "))
    # newstraintype = str(input("Enter a new type of strain(Hybrid, Indica, Sativa): "))
    # data2.extend({'strain':str(newstrain), 'type':str(newstraintype)})
    newlist = sorted(data2, key=lambda d: d['type'])
    print(newlist)

    newlist2 = sorted(data2, key=lambda y: y['type'])
    print(newlist2)
    print()
    print(data2[0])
    print()


dictionaryWork()
print()
print()

strings = ["Machew", "Raven", "LUCKI", "Baby Smoove", "Mills", "Purple Kush"]
sorted_strings = sort_by_last_char(strings)
print("Example 1: ")
print(sorted_strings)
print()
string2 = ["Sour Tangie", "Lavender", "Jack Herer", "Cream Soda", "Alaskan Thunder Fuck", "Biscotti", "Blue Dream",
           "Pineapple Express", "Biscotti", "Bruce Banner"]
sorted_string2 = sort_by_first_char(string2)
print("Example 2: ")
print(sorted_string2)

print()
print("For Loop Work: ")
forloopworked(string2)
print()
print()
if __name__ == '__main__':
    dictionaryWork()


# peep how the string LUCKI is captial and is print first in the output for the sorted strings
# ITS BECAUSE ITS IN UPPERCASE AND UPPERCASE LETTERS COME FIRST

# Create luh program that generates 200 random numbers, stores them into a dictionary and separates them if its even or odd
def randoms():
    x = int(0)
    l = []
    l2 = []
    l3 = []
    kp = int(0)
    kp2 = int(0)
    dic = {}
    for nums in range(50):
        nums = random.randint(12, 56)
        l.append(nums)
        if nums % 2 == 0:
            l2.append(nums)
        elif nums % 2 != 0:
            l3.append(nums)
    print(f"Original List: {l}")
    print(f'List of evens: {l2}')
    print(f'List of odds: {l3}')
    print()
    dictonary = {"Evens": l2, "Odds": l3}
    for items in sorted(dictonary.values()):
        print(items)
    print()
    print(f"Dictionary: {dictonary}")
    print(type(dictonary))
    my_strains = dictonary["Evens"][1]
    print(my_strains)
    print()
    print("Mastery Was Shown Here: ")
    for evenorodd, numbers in dictonary.items():
        for num in numbers:
            print(evenorodd, num)


randoms()


def cleanup():
    list = []
    evens = []
    odds = []
    # dic = {}
    maxrange = int(57)
    minrange = int(20)
    for nums in range(minrange, maxrange):
        nums = random.randint(1, 76)
        list.append(nums)
    x = int(0)
    print("Original List: ")
    for num in list:
        print(f"{x + 1}. {num}")
    for num in list:
        if (num % 2 == 0):
            evens.append(num)
        elif (num % 2 != 0):
            odds.append(num)
    print(f'Evens: {evens}')
    print(f'Odds: {odds}')
    print()
    dic = {"Even": evens, "Odd": odds}
    index = int(0)
    for x, y in sorted(dic.items()):
        for lucki in y:
            print(f'{index + 1}. {x} - {lucki}')
            index += 1
    print()
    index2 = int(0)
    print("Printing the evens: ")
    for x, y in sorted(dic.items()):
        for lucki in y:
            if x == 'Even':
                print(f'{index2 + 1}. {x} ☚ {lucki}', end=' ---- ')
                index2 += 1
    print()
    print("Printing The Odds: ")
    print(f"Dictionary of the Evens And Odds List: {dic}")


if __name__ == '__main__':
    cleanup()


class machew:
    def __init__(self):
        self.fname = input("Enter your first name: ")
        self.mname = input("Enter your middle name: ")
        self.lname = input("Enter your last name: ")
        self.listOfSongs = []
        self.Lucki = []
        self.BabySmoove = []
        self.dickOfBothArtist = {}

    def fullname(self):
        fullname = self.fname + " " + self.mname + " " + self.lname
        self.fullname = fullname

    def getInitials(self):
        Finital = self.fname[0:1]
        Minital = self.fname[0:1]
        Linital = self.fname[0:1]
        UserInitals = Finital + Minital + Linital

    def getfullName(self):
        print()
        return "Full Name: " + self.fullname

    def getSongs(self):
        index = int(0)
        count = int(input("How many songs are your favorite by LUCKI: "))
        for songs in range(int(count)):
            songs = str(input(f"{index + 1}. Enter your favorite songs by LUCKI: "))
            self.Lucki.append(str(songs))
            index += 1
        print()
        index2 = int(0)
        count2 = int(input("How many songs are your favorite by Baby Smoove: "))
        for songs in range(int(count2)):
            songs = input(f"{index2 + 1}.Enter your favorite songs by Baby Smoove:")
            self.BabySmoove.append(str(songs))
            index2 += 1

        self.dickOfBothArtist = {"LUCKI": self.Lucki, "Baby Smoove": self.BabySmoove}

        print()
        print("Printing The Dictionary Of Both Artist: ")
        print(self.dickOfBothArtist)

        index = int(0)
        print()
        print("Printing All LUCKI Songs: ")
        for x, y in self.dickOfBothArtist.items():
            for tune in y:
                if x == "LUCKI":
                    print(f'{index + 1}. {tune}')
                    index += 1


macChicken = machew()
# macChicken.fullname()
print(macChicken.getfullName())
macChicken.getSongs()


# =====================================================================================
#           Searching
# Linear Search
# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
# print arr.index(x)

# If you want to implement Linear Search in python

# Linearly search x in arr[]
# If x is present then return its location
# else return -1

def search():
    arr = []
    found = False
    searchVal = input("Enter a number to search for: ")
    for nums in range(20):
        nums = random.randint(1, 56)
        arr.append(nums)
    for i in range(len(arr)):
        if arr[i] == searchVal:
            found = True
    return found


print(search())
# Binary Search
