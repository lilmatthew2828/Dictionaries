'''
Matthew Kilpatrick
4/6/24
Chapter 9.2
Mastering Sets
'''
from tabulate import tabulate
import random
import pygame
# Set - A collection which is ORDERED, unindexed.
# No Duplicate Values
'''
All elements in a set must be unique, No two elements can have the same value
Sets are unordered, which means that the elements in a set are not stored in any particular order
The elements that are stored in a set can be a different data types
'''
evens = []
odds = []
dick = {}
for nums in range(34):
    nums = random.randint(12, 56)
    if (nums % 2 == 0):
        evens.append(nums)
    elif (nums % 2 != 0):
        odds.append(nums)

print(f'Evens = {evens}')
print(f'Odds = {odds}')
print()
matthewsartist = ["LUCKI", "Babyface Ray", "Warhol.SS", "Baby Smoove", "Young Nudy", "Pi'erre Bourne", "Yung Bans", "Destroy Lonely", "Future", "Yeat"]
matthewsSongs = ["Goodfellas","3D Outro", "Nigo","All Love", "Archived Celine"]
ravensartist = ["Tony Shhnow", "Yeat", "Young Nudy", "Destroy Lonely", "ICYTWAT", "Lil Candypaint", "Faye Webster", "The Killers", "Cold Play", "PinkPanthers"]
ravenssongs = ["Bruises", "Hunchoz" , "Mysëlf", "Final Boss Music", "Take Me Apart", "Type Money"]
matthewsdick={}
ravensdick ={}
matthewsdick.update({"Matthews Artist":matthewsartist})
matthewsdick.update({"Matthews Songs":matthewsSongs})
ravensdick.update({"Ravens Artist":ravensartist})
ravensdick.update({"Ravens Songs":ravenssongs})
dick.update({"Machews List":matthewsdick})
dick.update({"Ravens List":ravensdick})
print("Menu: ")
index = int(0)
for data in dick:
    print(f'{index+1}. {data}')
    index += 1
print()
options = int(input("Enter a list to print from: "))
if(options == 1):
    print("Printing From Machews List: ")
    for menu,menuitems in dick.items():
        if(menu == "Machews List"):
            print((menu))
            print("--------------------------------")
            for items,songs in menuitems.items():
                print(items)
                for x in songs:
                    print(x)
                print()
            print()
elif(options == 2):
    print("Printing From Ravens List: ")
    for menu, menuitems in dick.items():
        if (menu == "Ravens List"):
            print((menu))
            print("--------------------------------")
            for items, songs in menuitems.items():
                print(items)
                for x in songs:
                    print(x)
                print()
            print()
class SetsExample:
    def __init__(self):
        self.artistNsongs = None
        self.artist = {"LUCKI", "Destroy Lonely", "Warhol.ss"}
        self.songs = {"GOODFELLAS", "if looks could kill", "SECOND NATURE"}

    def add(self):
        option = int(input("Do you want to add a song, a artist, or both: "))
        if (option == 1):  # song:
            song = str(input("Enter a song to add to the set: "))
            self.songs.add(song)
        elif (option == 2):  # artist
            artist = str(input("Enter a artist to add to the list: "))
            self.artist.add(artist)
        elif (option == 3):  # both
            song = str(input("Enter a song to add to the set: "))
            artist = str(input("Enter a artist to add to the list: "))
            self.songs.add(song)
            self.artist.add(artist)

    def remove(self):
        option = int(input("Do you want to remove a song, a artist, or both: "))
        if (option == 1):  # song:
            song = str(input("Enter a song to remove to the set: "))
            self.songs.remove(song)
        elif (option == 2):  # artist
            artist = str(input("Enter a artist to remove to the list: "))
            self.artist.remove(artist)
        elif (option == 3):  # both
            song = str(input("Enter a song to remove to the set: "))
            artist = str(input("Enter a artist to remove to the list: "))
            self.songs.remove(song)
            self.artist.remove(artist)

    def clear(self):
        option = int(input("Do you want clear the songs, the artist or both: "))
        if (option == 1):  # Clear the song set:
            self.songs.clear()
        elif (option == 2):  # Clear the artist set
            self.artist.clear()
        elif (option == 3):  # clear both sets
            self.songs.clear()
            self.artist.clear()

    def update(self):
        option = int(input("Would you like to add the artists to songs or songs to artists"))
        if (option == 1):
            self.songs.update(self.artist)  # adding the artist, which is in the parenthesis to the songs
        elif (option == 2):
            self.artist.update(self.songs)  # adding the songs, which is in the parenthesis to the artists

    def Union(self):
        self.artistNsongs = self.artist.union(self.songs)
        index = int(0)
        print()
        print("Union Of Artist And Songs Sets: ")
        for artistAndSongs in self.artistNsongs:
            print(f'{index + 1}. {artistAndSongs}')
            index += 1

    def print(self):
        fuck = int(input("Do you want to print the artist, the songs, or both: "))
        if(fuck == 1):
            x = int(0)
            print()
            print("The Artists: ")
            for artist in self.artist:
                print(f"{x+1}. {artist}")
                x += 1
        elif(fuck == 2):
            y = int(0)
            print()
            print("The Songs: ")
            for song in self.songs:
                print(f'{y+1}. {song}')
                y += 1
        elif(fuck ==3):
            twin = int(0)
            print()
            print("The Artist And Their Mother Fucking Crank: ")
            artistnsongs = self.artist.union(self.songs)
            for kingsncranks in artistnsongs:
                print(f"{twin+1}. {kingsncranks} ")
                twin += 1


def ravenismybby():
    PenisEnvy = SetsExample()
    PenisEnvy.add()
    PenisEnvy.remove()
    PenisEnvy.update()
    PenisEnvy.Union()
    PenisEnvy.print()

#ravenismybby()
def setsExample2():
    file = open("Sets.txt", 'w')
    file.write("This is the text file for the sets we finna fuck around with: \n")
    MachewsTop10 = {"LUCKI", "Babyface Ray", "Warhol.SS", "Baby Smoove", "Young Nudy", "Pi'erre Bourne", "Yung Bans", "Destroy Lonely", "Future", "Yeat"}
    RavensTop10 = {"Tony Shhnow", "Yeat", "Young Nudy", "Destroy Lonely", "ICYTWAT", "Lil Candypaint", "Faye Webster", "The Killers", "Cold Play", "PinkPanthers"}
    print()
    file.write('\n')
    print(f'Original Machew: {MachewsTop10}') # EVERYTIME YOU PRINT A SET IT PRINTS UNORDERED
    file.write(f'Original Machew: {MachewsTop10}\n')
    print(f'Original Raven: {RavensTop10}')
    file.write(f'Original Raven: {RavensTop10}\n')
    print()
    file.write('\n')
    print("1. Union ( | ) Operator Work: ")
    file.write("1. Union ( | ) Operator Work: \n")
    JoiningMachewToRaven = MachewsTop10.union(RavensTop10)
    JoiningRavenToMachew = RavensTop10.union(MachewsTop10)
    print(f"Machew With Ravens Artists: {JoiningMachewToRaven}")
    file.write(f"Machew With Ravens Artists: {JoiningMachewToRaven}\n")
    print(f"Raven With Machews Artists: {JoiningRavenToMachew}")
    file.write(f"Raven With Machews Artists: {JoiningRavenToMachew}\n")
    print()
    file.write("\n")
    print("2. Difference ( - ) Operator Work: ")
    file.write("2. Difference ( - ) Operator Work: \n")
    difference1 = MachewsTop10.difference(RavensTop10) # this line will only print what I have, meaning, if we both i have lonely it wont print lonely
    difference2 = RavensTop10.difference(MachewsTop10) # this line will only print what raven has
    difference22 = RavensTop10 - MachewsTop10 # Alternate way of getting the difference of two sets
    print(f'Printing The Artist In Machews top 10 That Are Not In Ravens Top 10: {difference1}')
    file.write(f'Printing The Artist In Machews top 10 That Are Not In Ravens Top 10: {difference1}\n')
    print(f'Printing The Artist In Ravens top 10 but in Machews: {difference2}')
    file.write(f'Printing The Artist In Ravens top 10 but in Machews: {difference2}\n')
    print(f"Printing The Artist That Appear In Ravens Top 10 but not in Machew Top 10: {difference22}")
    file.write(f"Printing The Artist That Appear In Ravens Top 10 but not in Machew Top 10: {difference22}\n")
    print()
    file.write("\n")

    print(f'3. Intersection ( & ) Operator Work: ') # This operator prints whats in both sets
    file.write(f'3. Intersection ( & ) Operator Work: \n')
    MachewCommonRaven = MachewsTop10.intersection(RavensTop10)
    RavenCommonMachew = RavensTop10.intersection(MachewsTop10)
    print(f'Printing the artist that Machew have in common with Raven: {MachewCommonRaven}')
    print(f'Printing the artist that Raven have in common with Machew: {RavenCommonMachew}')
    file.write(f'Printing the artist that Machew have in common with Raven: {MachewCommonRaven}\n')
    file.write(f'Printing the artist that Raven have in common with Machew: {RavenCommonMachew}\n')
    print()
    file.write('\n')
    print("4. Adding N Artist To Either List: ")
    file.write('4. Adding N Artist To Either List: \n')
    option1 = int(input("Which would you like to add artist to?: (1) for machew, (2) for raven, 3 for nun: "))
    while(option1 > 3): # peep the greater than sign
        print("Invalid Bitch, 1 or 2")
        option1 = int(input("Which would you like to add artist to?: (1) for machew, (2) for raven: "))
    if(option1 == 1):
        numofArtist = int(input("How many artist would you like to add to Machews list: "))
        index = int(0)
        for artist in range(numofArtist):
            artist = str(input(f"{index+1}. Enter the name of the artist: "))
            index+=1
            MachewsTop10.add(artist)
    elif(option1 == 2):
        numofArtist = int(input("How many artist would you like to add to Ravens list: "))
        index = int(0)
        for artist in range(numofArtist):
            artist = str(input(f"{index + 1}. Enter the name of the artist: "))
            index += 1
            RavensTop10.add(artist)
    elif(option1 == 3):
        print("Respect you staying solid with your list")

    print()
    print("5. Removing From The List In Two Ways, .remove(), .discard()")
    file.write("5. Removing From The List In Two Ways, .remove(), .discard()\n")
    opt2 = int(input("Do you want to remove any artist from either list: "))
    if(opt2 == 1):
        removeValue1 = input("Enter an artist to remove from Machews set: ")
        while(removeValue1 not in MachewsTop10): # while your dumbass keeps entering values that are not exsistent in machews top 10
            print("Entered Value is not in the list, please try again lil nigga")
            removeValue1 = input("Enter an artist to remove from Machews List: ")
        MachewsTop10.remove(removeValue1)
        print("Printing Machew's Top 10 With Removed Element")
        print(MachewsTop10)
        file.write("Printing Machew's Top 10 With Removed Element\n")
        file.write(f'{MachewsTop10}\n')
        print()
        file.write('\n')
        print("Removing From The List Using The Discard Method: ")
        file.write("Removing From The List Using The Discard Method: \n")
        removeValue2 = input("Enter an artist to remove from Ravens set: ")
        while(removeValue2 not in RavensTop10):
            print("Dick, Try Again, Ion Know Who TF you just entered but they not in my babys top 10:")
            print("TRY AGAIN: ☺︎")
            removeValue2 = input("Enter an artist to remove from Ravens set: ")
        RavensTop10.discard(removeValue2)
        print("Printing Raven's Top 10 with the Removed Element:")
        print(RavensTop10)
        file.write("Printing Raven's Top 10 with the Removed Element:\n")
        file.write(f"{RavensTop10}\n")
    else:
        print("Good Choice, NO GREAT CHOICE")

    print()
    file.write('\n')
    print("6. Symmetric Difference ( ^ ) Operator: ") # The Symmetric Difference of two sets is a set that contains the elements that ARE NOT SHARED BY THE SETS
    file.write("6. Symmetric Difference ( ^ ) Operator: \n")
    symDiff = MachewsTop10.symmetric_difference(RavensTop10) # meaning its the elements thats in one set but not both:
    print(f'Printing the elements that are in {symDiff}') # The method will return a set that contains the artist that are found in either set, but not if the artist is in both, meaning it wont print yeat
    file.write(f'Printing the elements that are in {symDiff}\n')
    print()
    file.write('\n')
    print("7. Finding Subsets (<=) And Supersets ( >= ): ") # Say you have two sets and one of those sets contains all of the elements of the other set
    file.write("7. Finding Subsets (<=) And Supersets ( >= ): \n")
    # Example subset:
    machewSubset = {"LUCKI", "Warhol.SS"} # this is the newly created subset
    Ravensubset = {"Faye Webster", "Destroy Lonely", "Yeat"}
    print(f"Is the Machew Subset A subset of The OG Machew set: {machewSubset.issubset(MachewsTop10)} \n") # here the machewSubset is a subset of the og set of machew top 10 artist
    file.write(f"Is the Machew Subset A subset of The OG Machew set: {machewSubset.issubset(MachewsTop10)} \n")
    print(f'Is The OG Raven Set A SUPERSET to the RavenSubset in line 208: {RavensTop10 >= (Ravensubset)}')
    file.write(f'Is The OG Raven Set A SUPERSET to the RavenSubset in line 208: {RavensTop10 >= (Ravensubset)}\n')
    print(f'Is The OG Raven Set A SUPERSET to the RavenSubset in line 208: {RavensTop10.issuperset(Ravensubset)}\n '
          f'This is the same thing as the line above but i used the regular operator.\n')
    file.write(f'Is The OG Raven Set A SUPERSET to the RavenSubset in line 208: {RavensTop10.issuperset(Ravensubset)}\n '
          f'This is the same thing as the line above but i used the regular operator.\n')
    file.close()
setsExample2()


