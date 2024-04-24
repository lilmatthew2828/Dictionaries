'''
Matthew Kilpatrick
4/6/24
This is a sets example but with mastery
'''
import random
from tabulate import tabulate
import pygame
import pandas
import numpy as np
print(pandas.__version__)

class setWithStrings:
    def __init__(self):
        self.dick = {}
        self.user1 = "Machew"
        self.user2 = "Raven"
        self.matthewsDick = {}
        self.ravensDick = {}
        self.matthewsartist = []
        self.matthewsongs = []
        self.ravensartist = []
        self.ravenssongs = []
        self.file = open("Set2.txt", "w")

    def getArtist(self):
        count1 = int(input("How many artist do you want to enter for matthew: "))
        count2 = int(input("How many songs do you want to enter for matthew: "))
        x = int(0)
        y = int(0)
        for artist in range(count1):
            artist = str(input(f"{x + 1}. Enter the artist: "))
            self.matthewsartist.append(artist)
            for songs in range(count2):
                songs = str(input(f"\t{y + 1}. Enter the songs: "))
                self.matthewsongs.append(songs)
                y += 1
            x += 1
            y = 0
        print()
        count3 = int(input("How many artist do you want to enter for Raven: "))
        count4 = int(input("How many songs do you want to enter for raven: "))
        kp = int(0)
        twin = int(0)
        for artist in range(count3):
            artist = str(input(f"{kp + 1}. Enter the artist: "))
            self.ravensartist.append(artist)
            for songs in range(count4):
                songs = str(input(f"\t{twin + 1}. Enter the songs: "))
                self.ravenssongs.append(songs)
                twin += 1
            kp += 1
            twin = 0
        print()
        self.matthewsDick.update({"Machews Artist": self.matthewsartist})
        self.ravensDick.update({"Ravens Artist": self.ravensartist})
        self.matthewsDick.update({"Matthews Songs": self.matthewsongs})
        self.ravensDick.update({"Ravens Songs": self.ravenssongs})
        self.dick.update({"Matthews Lists": self.matthewsDick})
        self.dick.update({"Ravens List": self.ravensDick})

    def printDick(self):
        print()
        index = int(0)
        i = int(0)
        k = int(0)
        print("Options Of List To Print:")
        for menu in self.dick:
            print(f'{index + 1}. {menu}')
            index += 1
        print()
        luckismyking = int(input("1. To Print From Matthew List\n"
                                 "2. To print From Ravens List: "))
        if (luckismyking == 1):
            print("Printing Machews List of Data: ")
            self.file.write(f"Printing Machews List of Data: \n")
            for menu, items in self.dick.items():
                if (menu == "Matthews Lists"):
                    print(menu)
                    self.file.write(f'{menu}\n')
                    for data, list in items.items():
                        print(f'\t{data}')
                        self.file.write(f'\t{data}\n')
                        for songs in list:
                            print(f'\t\t{songs}')
                            self.file.write(f'\t\t{songs}\n')
                    print()
                    self.file.write('\n')
        elif (luckismyking == 2):
            print("Print from Ravens List of Data: ")
            self.file.write("Print from Ravens List of Data: \n")
            for menu, items in self.dick.items():
                if (menu == "Ravens List"):
                    print(menu)
                    self.file.write(f'{menu}\n')
                    for data, list in items.items():
                        print(f'\t{data}')
                        self.file.write(f'\t{data}\n')
                        for songs in list:
                            print(f'\t\t{songs}')
                            self.file.write(f'\t\t{songs}\n')
                    print()
                    self.file.write('\n')
        self.file.close()

    def readingFromFile(self):
        print()
        print("Reading From The File: ")
        txtfile = open('Set2.txt', 'r')
        for data in txtfile:
            print(data, end=" ")
        txtfile.close()


def main():
    Machew = setWithStrings()
    Machew.getArtist()
    Machew.printDick()
    Machew.readingFromFile()


#if __name__ == "__main__":
    #main()
'''
Write an algorithm that does the following
1. Accepts the age of users in a class////input
2. Finds the sum// calculation
3. Find the average// calculation
4. Gets the youngest person// determine
5. Display /// print
'''
print("Class Problem Quicky Yemme!!!")

# More Mastery
class Age:
    def __init__(self):
        self.count = int(input("How many Users are in this class today ?: "))
        self.users = {}
        self.pair = ()
        self.sumOfage = int(0)
        self.average = float(0.0)
        self.youngest = self.users[0]

    def getUserNamesNAges(self):
        for names in range(self.count):
            names = str(input("Enter your name: "))
            age = int(input("Enter your age: "))
            self.pair = (names, age)
            self.users.update({self.pair})
        print("Peep The pairs in the dictionary")
        print(self.users)

    def getSumofAllAges(self):
        print("Note How IM extracting the data in the various for loops")
        index = int(0)
        print("These are the keys of the dictionary")
        for names in self.users: # This will just get the names of the dictionary which are the keys of the dictionary
            print(f'{index+1}. {names}')
            index += 1
        print("We will now go inside of the keys to extract their values: ")
        x = int(0)
        for names, age in self.users.items():
            print(f"{x+1}. {names} - {age} ")
            x += 1
        print("Now we can iterate through the ages and sum them all together: ")
        for names, age in self.users.items():
            self.sumOfage += age
    def getSum(self):
        return self.sumOfage
    def alternateWayOfGetTheValuesOfADictionary(self):
        index = int(0)
        print()
        print("This is a more easy way and clean way of getting the total of all the ages/values of the keys in the dictionary: ")
        print("We will be strictly extracting just the values and not the keys")
        print("This just get the keys: ")
        for names in self.users:
            print(names)
        print()
        print("This will print the pairs in the dictionary: ")
        for names, ages in self.users.items():
            print(names, ages)
        print()
        print("This will also just print the names/the values: ")
        for names in self.users.keys():
            print(names)
        print()
        print("This just prints the ages: ")
        for ages in self.users.values():
            print(ages)

    def getAverage(self):
        print("This is getting the avergae formula: \n"
              "average = sum/number of elements")
        print()
        self.average = self.sumOfage / self.count
    def returnAvg(self):
        return self.average

    def findTheYoungest(self):
        # We will be doing this in two ways:
        for age in self.users.values():
            if age < self.youngest:
                self.youngest = age
        return self.youngest


Macchicken = Age()
Macchicken.getUserNamesNAges()
Macchicken.getSumofAllAges()
print(f'The total sum of all the ages: {Macchicken.getSum()}')
Macchicken.alternateWayOfGetTheValuesOfADictionary()
Macchicken.getAverage()
print(f"The Average of the ages: {Macchicken.returnAvg()}")
print(f'The Youngest: {Macchicken.findTheYoungest()}')


'''
Write an algorithm that designs a function that accepts a list of numbers as an argument. 
The function should recursively calculate the sum of all the numbers in the list and return that value.
'''

'''
Write an algorithm that asks the user to enter a series of single-digit numbers with nothing separating them. 
The algoritm should display the sum of all the single digit numbers in the string. 
For example, if the user enters 1234, the method should return 10, which is the sum of 1, 2, 3, and 4.
'''

'''
Write an algorithm with a loop that asks the user to enter a series of positive numbers. 
The user should enter a negative number to signal the end of the series. 
After all the positive numbers have been entered, the program should display their sum.

'''