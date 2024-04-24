import random
from tabulate import tabulate
# Matthew Kilpatrick
# 2 - 24 - 24
# Warming up / COOKING YEMME

# ASKING USER FOR A NUMBER OF ARTIST THEY WANT TO ENTER AND WRITING IT TO A FILE:
# Take the first and last initial of each artist entered
row = int(6)
columns = int(9)
symbol = '$'
for i in range(row):
    for j in range(columns):
        print(symbol, end= "")  # To prevent a new print line being made use the " , end= ""
    print()
def raven():
    artistFile = open('Artist.txt', 'w') # open the file
    index = int(0) # the index for user input
    index2 = int(0) # the index  the will be written to the file
    index3 = int(0)
    index4 = int(0)
    num_of_artist = int(input("How many artist would you like to enter: ")) # rows
    num_of_songs = int(input(("How many songs would like to enter for each artist: "))) #columns
    list_of_artist = []
    list_of_songs = []
    for artist in range(0, num_of_artist):
        artist = str(input(f'{index+1}. Enter your top {num_of_artist} artists: '))
        list_of_artist.append(artist)
        index+=1
    print(list_of_artist)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"Now you're going to enter {num_of_songs} for each artist ")
    x = int(0)
    y = 0
    index5 = int(0)
    index6 = int(0)
    index7 = int(0)
    count = int(0)
    count2 = int(0)
    count3 = int(0)
    count4 = int(0)
    for artist in range(0, num_of_artist + 1)  and list_of_artist:
        artistFile.write(f'Artist {index7 +1}. {artist}\n')
        print(f'Artist {index2 +1}: {list_of_artist[count]}')
        for songs in range(0, num_of_songs) :
            songs = str(input(f'{index4+1}. Enter songs: '))
            list_of_songs.append(songs)
            artistFile.write(f'Song {index5+1}. {songs}\n')
            index4 += 1
            index5 += 1
            count2 += 1
        artistFile.write("\n")
        print()
        count +=1
        count2 =0
        x += 1
        y += 1
        index5 = 0
        index2 += 1
        index3 += 1
        index6 += 1
        index7 += 1
        index4 = 0
    print()
    print(list_of_artist)
    print(list_of_songs)
    artistFile.close()
#if  __name__  ==  '__main__' :
   # raven()

# Printing The File:
def RavenPrint():
    read_from_artist_file = open('Artist.txt', 'r')
    index = int(0)
    print() # Line For Spacing in the output
    print("Printing The File(Reading From:")
    for line in read_from_artist_file:
        mills = str(line)
        print(f'{mills}', end="")
        index += 1
    read_from_artist_file.close()
#if __name__  == '__main__':
    #RavenPrint()

def April16th():
    num_file = open("Numbers File", 'w')
    index = int(0)
    list_of_nums = []
    count_of_ranNums = int(input("How many range numbers do you want to generate: "))
    max = int(input("Enter a maximum: "))
    min = int(input("Enter a minim: "))
    if(min >= max):
        while(min>=max):
            print(f"Enter a minimum thats less than the max, {max}: ")
            min = int(input("Enter a minimum:"))
    print(f'Now the Program will generate {count_of_ranNums} random numbers that are between {min} and {max}.')
    for random_nums in range(0, count_of_ranNums+1):
        random_nums = random.randint(min,max)
        list_of_nums.append(random_nums)
        num_file.write(f"{random_nums}\n")
    num_file.close()
    print("List of Random Numbers: ")
    print(list_of_nums)
#if __name__ == '__main__':
   # April16th()
def April16thPrint():
    read_randNumFIle = open('Numbers File', 'r')
    index = int(0)
    print()# line for spacing in the output
    print("The Output of All the random Numbers: with index: ")
    for lines in read_randNumFIle:
        numbers = str(lines)
        print(f'{index+1}. {numbers}', end="")
        index+=1
    read_randNumFIle.close()
# if __name__ == '__main__':
    #April16thPrint()
def April16thPrintingInTables():
    index = int(0)
    string_evens = "Evens: "
    string_odds = "Odds: "
    string_allNumbers = "All Numbers: "
    reading_fromFile = open('Numbers File', 'r')
    print(f'{string_allNumbers : >10} {string_evens: >50} {string_odds: >60}')
    for lines in reading_fromFile:
        Lines = str(lines)
        print(f'{index+1:>10}. {Lines}')
        if(lines % 2 == 0 ):
            print(f'{index+1:>50}. {Lines}')
        elif(lines % 2 != 0):
            print(f'{index+1:>60}. {Lines}')
# if __name__ == '__main__':
    # April16thPrintingInTables()
def main():
    list_of_ranNums = []
    list_of_odd_ranNums = []
    list_of_even_ranNums = []
    count = int(input("Enter A Number Of Random Numbers: "))
    for nums in range(0, count+1):
        rannums = random.randint(1,1000) # generating random numbers between 1 and 999
        list_of_ranNums.append(rannums)
        if(rannums % 2 == 0): # validating even random numbers
            list_of_even_ranNums.append(rannums)
        elif(rannums % 2 != 0): # validating odd random numbers
            list_of_even_ranNums.append(rannums)
    print()
    print("OutPut:")
    alllist = [list_of_ranNums, list_of_odd_ranNums, list_of_even_ranNums]
    print("---------------------------------------------------------------------------------------------------------")
    print(tabulate(alllist))
    print("---------------------------------------------------------------------------------------------------------")
    index = int(0)
    print()
    string_evens = "Evens: "
    string_odds = "Odds: "
    string_allNumbers = "All Numbers: "
    print(f'{string_allNumbers : >10} {string_evens: >50} {string_odds: >60}')
    for lines in list_of_ranNums:
        print(f"{index+1}. {lines:>10}")
        if( lines % 2 == 0):
            print(f'{index+1}. {lines: >70}')
        elif(lines % 2 != 0):
            print(f'{index+1}. {lines:>140}')
        index += 1
if __name__ == '__main__':
    main()





















